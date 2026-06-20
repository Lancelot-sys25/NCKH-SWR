from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from sklearn.metrics import f1_score, hamming_loss, label_ranking_average_precision_score


@dataclass(frozen=True)
class MultiLabelMetrics:
    micro_f1: float
    macro_f1: float
    hamming_loss: float
    label_ranking_average_precision: float


def evaluate_multilabel(y_true: np.ndarray, y_score: np.ndarray, threshold: float = 0.5) -> MultiLabelMetrics:
    y_pred = (y_score >= threshold).astype(int)
    return MultiLabelMetrics(
        micro_f1=f1_score(y_true, y_pred, average="micro", zero_division=0),
        macro_f1=f1_score(y_true, y_pred, average="macro", zero_division=0),
        hamming_loss=hamming_loss(y_true, y_pred),
        label_ranking_average_precision=label_ranking_average_precision_score(y_true, y_score),
    )

