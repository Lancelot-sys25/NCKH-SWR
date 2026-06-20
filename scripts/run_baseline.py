import argparse

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

from quantum_re_nfr.data import load_standard_csv, sample_dataset
from quantum_re_nfr.metrics import evaluate_multilabel


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", help="Processed CSV file.")
    parser.add_argument("--sample", action="store_true", help="Run on built-in sample data.")
    args = parser.parse_args()

    bundle = sample_dataset() if args.sample else load_standard_csv(args.data)
    y = bundle.labels.to_numpy(dtype=int)

    vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=1)
    x = vectorizer.fit_transform(bundle.texts)
    clf = OneVsRestClassifier(LogisticRegression(max_iter=1000))
    clf.fit(x, y)
    y_score = np.vstack([estimator.predict_proba(x)[:, 1] for estimator in clf.estimators_]).T

    metrics = evaluate_multilabel(y, y_score)
    print(metrics)


if __name__ == "__main__":
    main()

