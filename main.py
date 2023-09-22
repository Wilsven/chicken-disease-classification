from chicken_disease_classification import logger
from chicken_disease_classification.pipeline.data_ingestion_pipeline import (
    STAGE_NAME,
    DataIngestionPipeline,
)

try:
    logger.info(f"{STAGE_NAME} has started")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.forward()
    logger.info(f"{STAGE_NAME} has completed")
except Exception as e:
    logger.exception(e)
    raise e
