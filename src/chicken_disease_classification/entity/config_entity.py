from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class BaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    image_size: list
    learning_rate: float
    include_top: bool
    weights: str
    classes: int


@dataclass(frozen=True)
class CallbacksConfig:
    root_dir: Path
    tensorboard_log_dir: Path
    checkpoints_file_path: Path


@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    epochs: int
    batch_size: int
    augmentation: bool
    image_size: list
