from chicken_disease_classification.constants import *
from chicken_disease_classification.entity.config_entity import DataIngestionConfig
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
            root_dir=data_ingestion.root_dir,
            source_url=data_ingestion.source_url,
            local_data_file=data_ingestion.local_data_file,
            unzip_dir=data_ingestion.unzip_dir,
        )

        return data_ingestion_config
