import argparse
from pathlib import Path

import pandas as pd

from quantum_re_nfr.config import LABELS


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Raw CSV with a text column and NFR label columns.")
    parser.add_argument("--output", required=True, help="Normalized CSV output path.")
    args = parser.parse_args()

    frame = pd.read_csv(args.input)
    if "text" not in frame.columns:
        raise ValueError("Input CSV must contain a 'text' column.")

    for label in LABELS:
        if label not in frame.columns:
            frame[label] = 0

    normalized = frame[["text", *LABELS]].copy()
    normalized["text"] = normalized["text"].fillna("").astype(str).str.strip()
    normalized = normalized[normalized["text"] != ""]
    normalized[LABELS] = normalized[LABELS].fillna(0).astype(int)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    normalized.to_csv(output, index=False)
    print(f"Wrote {len(normalized)} requirements to {output}")


if __name__ == "__main__":
    main()

