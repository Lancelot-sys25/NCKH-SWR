import numpy as np

from quantum_re_nfr.metrics import evaluate_multilabel


def test_evaluate_multilabel_returns_expected_fields():
    y_true = np.array([[1, 0], [0, 1], [1, 1]])
    y_score = np.array([[0.9, 0.1], [0.2, 0.8], [0.6, 0.7]])

    metrics = evaluate_multilabel(y_true, y_score)

    assert metrics.micro_f1 == 1.0
    assert metrics.macro_f1 == 1.0
    assert metrics.hamming_loss == 0.0
    assert metrics.label_ranking_average_precision == 1.0

