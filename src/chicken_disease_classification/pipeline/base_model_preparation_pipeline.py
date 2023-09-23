from chicken_disease_classification import logger
from chicken_disease_classification.components.base_model_preparation import BaseModel
from chicken_disease_classification.config.configuration import ConfigurationManager

STAGE_NAME_02 = "Base Model Preparation Pipeline"


class BaseModelPreparationPipeline:
    def __init__(self):
        pass

    def forward(self):
        """Runs the base model preparation pipeline."""
        config_manager = ConfigurationManager()
        base_model_config = config_manager.get_base_model_config()
        base_model = BaseModel(config=base_model_config)
        base_model.get_base_model()
        base_model.update_base_model()


if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME_02} has started")
        base_model_preparation_pipeline = BaseModelPreparationPipeline()
        base_model_preparation_pipeline.forward()
        logger.info(f"{STAGE_NAME_02} has completed")
    except Exception as e:
        logger.exception(e)
        raise e
