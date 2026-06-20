from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from .config import LABELS


@dataclass(frozen=True)
class DatasetBundle:
    texts: list[str]
    labels: pd.DataFrame


def sample_dataset() -> DatasetBundle:
    rows = [
        {
            "text": "The system shall encrypt all stored user passwords.",
            "security": 1,
            "performance": 0,
            "usability": 0,
            "reliability": 0,
            "maintainability": 0,
            "portability": 0,
            "operational": 0,
            "scalability": 0,
        },
        {
            "text": "The payment page shall respond within two seconds under normal load.",
            "security": 0,
            "performance": 1,
            "usability": 1,
            "reliability": 0,
            "maintainability": 0,
            "portability": 0,
            "operational": 0,
            "scalability": 1,
        },
        {
            "text": "The service shall remain available during a single node failure.",
            "security": 0,
            "performance": 0,
            "usability": 0,
            "reliability": 1,
            "maintainability": 0,
            "portability": 0,
            "operational": 1,
            "scalability": 0,
        },
        {
            "text": "Administrators shall be able to configure notification rules without code changes.",
            "security": 0,
            "performance": 0,
            "usability": 1,
            "reliability": 0,
            "maintainability": 1,
            "portability": 0,
            "operational": 1,
            "scalability": 0,
        },
        {
            "text": "The mobile client shall run on both Android and iOS devices.",
            "security": 0,
            "performance": 0,
            "usability": 0,
            "reliability": 0,
            "maintainability": 0,
            "portability": 1,
            "operational": 0,
            "scalability": 0,
        },
    ]
    frame = pd.DataFrame(rows)
    return DatasetBundle(
        texts=frame["text"].tolist(),
        labels=frame[LABELS],
    )


def load_standard_csv(path: str) -> DatasetBundle:
    frame = pd.read_csv(path)
    missing = {"text", *LABELS} - set(frame.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    return DatasetBundle(
        texts=frame["text"].fillna("").astype(str).tolist(),
        labels=frame[LABELS].astype(int),
    )
