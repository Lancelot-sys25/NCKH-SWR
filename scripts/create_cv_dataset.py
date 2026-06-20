import argparse
from pathlib import Path

import pandas as pd
from sklearn.model_selection import StratifiedKFold


def markdown_table(frame: pd.DataFrame) -> str:
    headers = list(frame.columns)
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for _, row in frame.iterrows():
        lines.append("| " + " | ".join(str(row[col]) for col in headers) + " |")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="data/processed/promise_exp_nfr_11class.csv",
        help="Processed CSV with text and label_name columns.",
    )
    parser.add_argument("--folds", type=int, default=10)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--out-dir", default="data/cv/promise_exp_10fold")
    args = parser.parse_args()

    input_path = Path(args.input)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    data = pd.read_csv(input_path)
    required = {"text", "label_name"}
    missing = required - set(data.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    data = data.reset_index(drop=True)
    data.insert(0, "sample_id", [f"REQ_{i + 1:04d}" for i in range(len(data))])
    data["fold"] = -1

    splitter = StratifiedKFold(n_splits=args.folds, shuffle=True, random_state=args.seed)
    for fold_index, (_, test_index) in enumerate(splitter.split(data["text"], data["label_name"]), start=1):
        data.loc[test_index, "fold"] = fold_index

    assignment_path = out_dir / "fold_assignments.csv"
    data.to_csv(assignment_path, index=False)

    summary_rows = []
    label_rows = []
    for fold in range(1, args.folds + 1):
        fold_dir = out_dir / f"fold_{fold:02d}"
        fold_dir.mkdir(parents=True, exist_ok=True)

        test_data = data[data["fold"] == fold].copy()
        train_data = data[data["fold"] != fold].copy()

        train_data.to_csv(fold_dir / "train.csv", index=False)
        test_data.to_csv(fold_dir / "test.csv", index=False)

        summary_rows.append(
            {
                "fold": fold,
                "train_rows": len(train_data),
                "test_rows": len(test_data),
                "train_labels": train_data["label_name"].nunique(),
                "test_labels": test_data["label_name"].nunique(),
            }
        )

        counts = test_data["label_name"].value_counts().sort_index()
        for label, count in counts.items():
            label_rows.append({"fold": fold, "label": label, "test_count": int(count)})

    summary = pd.DataFrame(summary_rows)
    label_summary = pd.DataFrame(label_rows)
    summary.to_csv(out_dir / "fold_summary.csv", index=False)
    label_summary.to_csv(out_dir / "fold_label_distribution.csv", index=False)

    readme = [
        "# PROMISE_exp 10-Fold Cross-Validation Dataset",
        "",
        "This folder contains stratified cross-validation splits for the PROMISE_exp NFR 11-class dataset.",
        "",
        "## Files",
        "",
        "- `fold_assignments.csv`: all samples with their assigned fold.",
        "- `fold_summary.csv`: train/test row counts for each fold.",
        "- `fold_label_distribution.csv`: label distribution in each test fold.",
        "- `fold_01/train.csv`, `fold_01/test.csv`, ..., `fold_10/train.csv`, `fold_10/test.csv`: ready-to-run train/test splits.",
        "",
        "## How to Use",
        "",
        "For fold 1:",
        "",
        "```text",
        "train: data/cv/promise_exp_10fold/fold_01/train.csv",
        "test : data/cv/promise_exp_10fold/fold_01/test.csv",
        "```",
        "",
        "Repeat for folds 1 to 10, then average the metrics.",
        "",
        "## Fold Summary",
        "",
        markdown_table(summary),
        "",
    ]
    (out_dir / "README.md").write_text("\n".join(readme), encoding="utf-8")

    print(f"Wrote cross-validation dataset to: {out_dir}")
    print(f"Wrote fold assignments: {assignment_path}")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()

