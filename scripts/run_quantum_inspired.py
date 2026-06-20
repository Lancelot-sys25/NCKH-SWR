import argparse

from quantum_re_nfr.config import LABELS
from quantum_re_nfr.data import load_standard_csv, sample_dataset
from quantum_re_nfr.explainability import top_feature_contributions
from quantum_re_nfr.metrics import evaluate_multilabel
from quantum_re_nfr.quantum_model import QuantumInspiredNFRClassifier


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", help="Processed CSV file.")
    parser.add_argument("--sample", action="store_true", help="Run on built-in sample data.")
    args = parser.parse_args()

    bundle = sample_dataset() if args.sample else load_standard_csv(args.data)
    y = bundle.labels.to_numpy(dtype=int)

    model = QuantumInspiredNFRClassifier()
    model.fit(bundle.texts, y)
    y_score = model.predict_proba(bundle.texts)

    print(evaluate_multilabel(y, y_score))
    print("\nExample explanation:")
    example_text = bundle.texts[0]
    for term, score in top_feature_contributions(model, example_text, LABELS.index("security")):
        print(f"security\t{term}\t{score:.4f}")


if __name__ == "__main__":
    main()

