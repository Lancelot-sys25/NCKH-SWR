import argparse
import csv
import json
import re
from dataclasses import asdict
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from quantum_re_nfr.explainability import top_feature_contributions
from quantum_re_nfr.quantum_model import QuantumInspiredNFRClassifier


CLASS_NAMES = {
    "A": "availability",
    "FT": "fault_tolerance",
    "L": "legal",
    "LF": "look_and_feel",
    "MN": "maintainability",
    "O": "operational",
    "PE": "performance",
    "PO": "portability",
    "SC": "scalability",
    "SE": "security",
    "US": "usability",
}

ESCAPE_REPLACEMENTS = {
    "\\92": "'",
    "\\93": '"',
    "\\94": '"',
}


def clean_text(text: str) -> str:
    cleaned = text.strip()
    for old, new in ESCAPE_REPLACEMENTS.items():
        cleaned = cleaned.replace(old, new)
    return " ".join(cleaned.split())


def parse_promise_arff(path: Path) -> pd.DataFrame:
    rows = []
    in_data = False
    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("%"):
            continue
        if line.lower() == "@data":
            in_data = True
            continue
        if not in_data or line.startswith("@"):
            continue
        try:
            project_id, text, label = next(csv.reader([line], quotechar="'", escapechar="\\"))
        except ValueError:
            continue
        rows.append(
            {
                "project_id": int(project_id),
                "text": clean_text(text),
                "label_code": label.strip(),
            }
        )
    frame = pd.DataFrame(rows)
    frame["label_name"] = frame["label_code"].map(CLASS_NAMES).fillna("functional")
    return frame


def class_metrics(name: str, y_true: np.ndarray, y_pred: np.ndarray) -> dict:
    return {
        "model": name,
        "accuracy": accuracy_score(y_true, y_pred),
        "macro_f1": f1_score(y_true, y_pred, average="macro", zero_division=0),
        "micro_f1": f1_score(y_true, y_pred, average="micro", zero_division=0),
        "weighted_f1": f1_score(y_true, y_pred, average="weighted", zero_division=0),
    }


def one_hot(labels: np.ndarray, classes: list[str]) -> np.ndarray:
    index = {label: i for i, label in enumerate(classes)}
    result = np.zeros((len(labels), len(classes)), dtype=int)
    for row, label in enumerate(labels):
        result[row, index[label]] = 1
    return result


def safe_train_test_split(texts: np.ndarray, labels: np.ndarray, test_size: float, seed: int):
    counts = pd.Series(labels).value_counts()
    rare_labels = set(counts[counts < 2].index)
    if not rare_labels:
        return train_test_split(
            texts,
            labels,
            test_size=test_size,
            random_state=seed,
            stratify=labels,
        )

    rare_mask = np.array([label in rare_labels for label in labels])
    common_texts = texts[~rare_mask]
    common_labels = labels[~rare_mask]
    rare_texts = texts[rare_mask]
    rare_y = labels[rare_mask]

    x_train, x_test, y_train, y_test = train_test_split(
        common_texts,
        common_labels,
        test_size=test_size,
        random_state=seed,
        stratify=common_labels,
    )
    x_train = np.concatenate([x_train, rare_texts])
    y_train = np.concatenate([y_train, rare_y])
    return x_train, x_test, y_train, y_test


def write_report(
    report_path: Path,
    raw_path: Path,
    dataset: pd.DataFrame,
    nfr_data: pd.DataFrame,
    metrics: list[dict],
    reports: dict[str, str],
    example: dict,
) -> None:
    metric_frame = pd.DataFrame(metrics)
    label_counts = nfr_data["label_name"].value_counts().rename_axis("label").reset_index(name="count")
    label_count_table = markdown_table(label_counts)
    metric_table = markdown_table(metric_frame, float_digits=4)

    lines = [
        "# PROMISE_exp NFR Experiment Report",
        "",
        "## Dataset",
        "",
        f"- Raw file: `{raw_path}`",
        f"- Total requirements parsed: `{len(dataset)}`",
        f"- NFR-only requirements used: `{len(nfr_data)}`",
        "- Task: 11-class NFR subtype classification.",
        "- Note: PROMISE_exp is single-label, so this experiment is an initial operationalization of the multi-label research idea.",
        "",
        "## Label Distribution",
        "",
        label_count_table,
        "",
        "## Overall Results",
        "",
        metric_table,
        "",
        "## Interpretation",
        "",
        "- `accuracy`: percentage of test requirements classified into the correct NFR subtype.",
        "- `macro_f1`: average F1 across classes; important when some NFR labels have few samples.",
        "- `micro_f1`: global F1 across all predictions; for single-label classification it is close to accuracy.",
        "- `weighted_f1`: F1 weighted by class size.",
        "",
        "## Quantum-Inspired Example Explanation",
        "",
        f"- Text: {example['text']}",
        f"- True label: `{example['true_label']}`",
        f"- Predicted label: `{example['predicted_label']}`",
        "",
        "| label | token/phrase | contribution |",
        "|---|---:|---:|",
    ]
    for item in example["contributions"]:
        lines.append(f"| {example['predicted_label']} | {item[0]} | {item[1]:.4f} |")

    lines.extend(
        [
            "",
            "## Per-Class Reports",
            "",
        ]
    )
    for model_name, text_report in reports.items():
        lines.extend(
            [
                f"### {model_name}",
                "",
                "```text",
                text_report,
                "```",
                "",
            ]
        )

    report_path.write_text("\n".join(lines), encoding="utf-8")


def markdown_table(frame: pd.DataFrame, float_digits: int | None = None) -> str:
    headers = list(frame.columns)
    rows = []
    for _, row in frame.iterrows():
        values = []
        for header in headers:
            value = row[header]
            if isinstance(value, float) and float_digits is not None:
                values.append(f"{value:.{float_digits}f}")
            else:
                values.append(str(value))
        rows.append(values)
    header_line = "| " + " | ".join(headers) + " |"
    separator = "| " + " | ".join(["---"] * len(headers)) + " |"
    row_lines = ["| " + " | ".join(values) + " |" for values in rows]
    return "\n".join([header_line, separator, *row_lines])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/raw/PROMISE_exp.arff")
    parser.add_argument("--name", help="Output prefix, for example promise_plus.")
    parser.add_argument("--test-size", type=float, default=0.30)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--out-dir", default="reports")
    args = parser.parse_args()

    raw_path = Path(args.data)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    output_name = args.name or re.sub(r"[^a-zA-Z0-9]+", "_", raw_path.stem).strip("_").lower()

    dataset = parse_promise_arff(raw_path)
    nfr_data = dataset[dataset["label_code"].isin(CLASS_NAMES)].copy()
    nfr_data = nfr_data.sort_values(["label_name", "text"]).reset_index(drop=True)
    processed_path = Path("data/processed") / f"{output_name}_nfr_11class.csv"
    processed_path.parent.mkdir(parents=True, exist_ok=True)
    nfr_data.to_csv(processed_path, index=False)

    classes = sorted(nfr_data["label_name"].unique())
    x_train, x_test, y_train, y_test = safe_train_test_split(
        nfr_data["text"].to_numpy(),
        nfr_data["label_name"].to_numpy(),
        test_size=args.test_size,
        seed=args.seed,
    )

    models = {
        "majority_baseline": DummyClassifier(strategy="most_frequent"),
        "tfidf_logistic_regression": Pipeline(
            [
                ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=1)),
                ("clf", LogisticRegression(max_iter=2000, class_weight="balanced")),
            ]
        ),
    }

    metrics = []
    reports = {}
    for model_name, model in models.items():
        model.fit(x_train, y_train)
        pred = model.predict(x_test)
        metrics.append(class_metrics(model_name, y_test, pred))
        reports[model_name] = classification_report(y_test, pred, labels=classes, zero_division=0)

    y_train_hot = one_hot(y_train, classes)
    quantum_model = QuantumInspiredNFRClassifier(threshold=0.5, random_state=args.seed)
    quantum_model.fit(list(x_train), y_train_hot)
    quantum_score = quantum_model.predict_proba(list(x_test))
    quantum_pred = np.array([classes[i] for i in quantum_score.argmax(axis=1)])
    metrics.append(class_metrics("quantum_inspired_projection", y_test, quantum_pred))
    reports["quantum_inspired_projection"] = classification_report(
        y_test, quantum_pred, labels=classes, zero_division=0
    )

    example_index = 0
    predicted_label = quantum_pred[example_index]
    predicted_label_index = classes.index(predicted_label)
    example = {
        "text": x_test[example_index],
        "true_label": y_test[example_index],
        "predicted_label": predicted_label,
        "contributions": top_feature_contributions(
            quantum_model,
            x_test[example_index],
            predicted_label_index,
            top_k=8,
        ),
    }

    metrics_path = out_dir / f"{output_name}_metrics.csv"
    report_path = out_dir / f"{output_name}_report.md"
    metadata_path = out_dir / f"{output_name}_metadata.json"

    pd.DataFrame(metrics).to_csv(metrics_path, index=False)
    write_report(report_path, raw_path, dataset, nfr_data, metrics, reports, example)
    metadata_path.write_text(
        json.dumps(
            {
                "source": str(raw_path),
                "all_rows": int(len(dataset)),
                "nfr_rows": int(len(nfr_data)),
                "classes": classes,
                "test_size": args.test_size,
                "seed": args.seed,
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    print(f"Wrote processed data: {processed_path}")
    print(f"Wrote metrics: {metrics_path}")
    print(f"Wrote report: {report_path}")
    print(pd.DataFrame(metrics).to_string(index=False))


if __name__ == "__main__":
    main()
