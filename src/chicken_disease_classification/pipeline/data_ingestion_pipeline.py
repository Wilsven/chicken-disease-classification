from chicken_disease_classification.components.data_ingestion import DataIngestion
from chicken_disease_classification.config.configuration import ConfigurationManager
from chicken_disease_classification import logger


STAGE_NAME = "Data Ingestion Pipeline"


class DataIngestionPipeline:
    def __init__(self):
        pass

    def forward(self):
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME} has started")
        data_ingestion_pipeline = DataIngestionPipeline()
        data_ingestion_pipeline.forward()
        logger.info(f"{STAGE_NAME} has completed")
    except Exception as e:
        logger.exception(e)
        raise e
