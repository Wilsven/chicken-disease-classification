import os
import urllib.request as request
import zipfile

from chicken_disease_classification import logger
from chicken_disease_classification.entity.config_entity import DataIngestionConfig
from chicken_disease_classification.utils.common import get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """Downloads the zipped data file if it does not already exist."""
        if not os.path.exists(self.config.local_data_file):
            file_name, headers = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file,
            )
            logger.info(f"{file_name} downloaded with the following info: \n{headers}")
        else:
            logger.info(
                f"File already exists of size: {get_size(self.config.local_data_file)}"
            )

    def extract_zip_file(self):
        """Extracts the contents from zipped file.

        Creates a directory if it does not already exist
        and extracts the contents fo the zipped file into the directory.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as f:
            f.extractall(unzip_path)
