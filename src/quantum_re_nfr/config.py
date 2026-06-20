from dataclasses import dataclass
from pathlib import Path


LABELS = [
    "security",
    "performance",
    "usability",
    "reliability",
    "maintainability",
    "portability",
    "operational",
    "scalability",
]


@dataclass(frozen=True)
class ProjectConfig:
    root_dir: Path
    raw_data_dir: Path
    processed_data_dir: Path
    labels: tuple[str, ...] = tuple(LABELS)
    random_seed: int = 42


def default_config() -> ProjectConfig:
    root = Path(__file__).resolve().parents[2]
    return ProjectConfig(
        root_dir=root,
        raw_data_dir=root / "data" / "raw",
        processed_data_dir=root / "data" / "processed",
    )

