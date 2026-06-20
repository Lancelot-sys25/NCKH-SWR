from __future__ import annotations

import numpy as np


def top_feature_contributions(model, text: str, label_index: int, top_k: int = 8) -> list[tuple[str, float]]:
    vector = model.vectorizer.transform([text]).toarray()[0]
    norm = np.linalg.norm(vector)
    state = vector / norm if norm else vector
    label_basis = model.label_basis_[label_index]
    contributions = state * label_basis
    names = np.array(model.vectorizer.get_feature_names_out())
    top_indices = np.argsort(np.abs(contributions))[::-1][:top_k]
    return [(names[i], float(contributions[i])) for i in top_indices if contributions[i] != 0]

