import os

from chicken_disease_classification.constants import *
from chicken_disease_classification.entity.config_entity import (
    BaseModelConfig,
    CallbacksConfig,
    DataIngestionConfig,
    EvaluationConfig,
    TrainingConfig,
)
from chicken_disease_classification.utils.common import create_directories, read_yaml


class ConfigurationManager:
    def __init__(
        self,
        config_file_path: Path = CONFIG_FILE_PATH,
        params_file_path: Path = PARAMS_FILE_PATH,
    ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Creates the root directory if it doesn't already exist
        and returns the configuration for data ingestion.

        Returns:
            DataIngestionConfig: Configuration for data ingestion.
        """
        data_ingestion = self.config.data_ingestion

        create_directories([data_ingestion.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(data_ingestion.root_dir),
            source_url=str(data_ingestion.source_url),
            local_data_file=Path(data_ingestion.local_data_file),
            unzip_dir=Path(data_ingestion.unzip_dir),
        )

        return data_ingestion_config

    def get_base_model_config(self) -> BaseModelConfig:
        """
        Creates the root directory if it doesn't already exist
        and returns the configuration for the base model.

        Returns:
            BaseModelConfig: Configuration for base model.
        """
        base_model_preparation = self.config.base_model_preparation
        params = self.params

        create_directories([base_model_preparation.root_dir])

        base_model_config = BaseModelConfig(
            root_dir=Path(base_model_preparation.root_dir),
            base_model_path=Path(base_model_preparation.base_model_path),
            updated_base_model_path=Path(
                base_model_preparation.updated_base_model_path
            ),
            image_size=params.IMAGE_SIZE,
            learning_rate=params.LEARNING_RATE,
            include_top=params.INCLUDE_TOP,
            weights=params.WEIGHTS,
            classes=params.CLASSES,
        )

        return base_model_config

    def get_callbacks_config(self) -> CallbacksConfig:
        """
        Creates the root directory and tensorboard log directory if they
        don't already exist and returns the configuration for the callbacks.

        Returns:
            CallbacksConfig: Configuration for callbacks.
        """
        callbacks_preparation = self.config.callbacks_preparation

        create_directories(
            [callbacks_preparation.root_dir, callbacks_preparation.tensorboard_log_dir]
        )

        callbacks_config = CallbacksConfig(
            root_dir=Path(callbacks_preparation.root_dir),
            tensorboard_log_dir=Path(callbacks_preparation.tensorboard_log_dir),
            checkpoints_file_path=Path(callbacks_preparation.checkpoints_file_path),
        )

        return callbacks_config

    def get_model_training_config(self) -> TrainingConfig:
        """
        Creates the root directory if it doesn't already exist
        and returns the configuration for model training.

        Returns:
            TrainingConfig: Configuration for model training.
        """
        model_training = self.config.model_training
        base_model_preparation = self.config.base_model_preparation
        params = self.params

        training_data = os.path.join(
            self.config.data_ingestion.unzip_dir, "Chicken-fecal-images"
        )

        create_directories([model_training.root_dir])

        model_training_config = TrainingConfig(
            root_dir=Path(model_training.root_dir),
            trained_model_path=Path(model_training.trained_model_path),
            updated_base_model_path=Path(
                base_model_preparation.updated_base_model_path
            ),
            training_data=Path(training_data),
            epochs=params.EPOCHS,
            batch_size=params.BATCH_SIZE,
            augmentation=params.AUGMENTATION,
            image_size=params.IMAGE_SIZE,
        )

        return model_training_config

    def get_evaluation_config(self) -> EvaluationConfig:
        training_data = os.path.join(
            self.config.data_ingestion.unzip_dir, "Chicken-fecal-images"
        )

        evaluation_config = EvaluationConfig(
            path_to_model=Path(self.config.model_training.trained_model_path),
            training_data=Path(training_data),
            all_params=self.params,
            image_size=self.params.IMAGE_SIZE,
            batch_size=self.params.BATCH_SIZE,
        )

        return evaluation_config
