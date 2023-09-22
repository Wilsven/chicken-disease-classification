from chicken_disease_classification.constants import *
from chicken_disease_classification.entity.config_entity import (
    BaseModelConfig,
    DataIngestionConfig,
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
        Creates the root directory and returns
        the configuration for data ingestion.

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
        base_model_preparation = self.config.base_model_preparation

        create_directories([base_model_preparation.root_dir])

        base_model_config = BaseModelConfig(
            root_dir=Path(base_model_preparation.root_dir),
            base_model_path=Path(base_model_preparation.base_model_path),
            updated_base_model_path=Path(
                base_model_preparation.updated_base_model_path
            ),
            image_size=self.params.IMAGE_SIZE,
            learning_rate=self.params.LEARNING_RATE,
            include_top=self.params.INCLUDE_TOP,
            weights=self.params.WEIGHTS,
            classes=self.params.CLASSES,
        )

        return base_model_config
