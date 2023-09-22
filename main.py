from chicken_disease_classification import logger
from chicken_disease_classification.pipeline.base_model_preparation_pipeline import (
    STAGE_NAME_02,
    BaseModelPreparationPipeline,
)
from chicken_disease_classification.pipeline.data_ingestion_pipeline import (
    STAGE_NAME_01,
    DataIngestionPipeline,
)

try:
    logger.info(f"{STAGE_NAME_01} has started")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.forward()
    logger.info(f"{STAGE_NAME_01} has completed")
except Exception as e:
    logger.exception(e)
    raise e

try:
    logger.info(f"{STAGE_NAME_02} has started")
    base_model_preparation_pipeline = BaseModelPreparationPipeline()
    base_model_preparation_pipeline.forward()
    logger.info(f"{STAGE_NAME_02} has completed")
except Exception as e:
    logger.exception(e)
    raise e
