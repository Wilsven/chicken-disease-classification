from chicken_disease_classification import logger
from chicken_disease_classification.components.callbacks_preparation import Callbacks
from chicken_disease_classification.components.model_training import Training
from chicken_disease_classification.config.configuration import ConfigurationManager

STAGE_NAME_03 = "Model Training Pipeline"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def forward(self):
        """Runs the model training pipeline."""
        config_manager = ConfigurationManager()

        callbacks_config = config_manager.get_callbacks_config()
        callbacks = Callbacks(config=callbacks_config)
        callbacks_list = callbacks.get_tb_ckpt_callbacks()

        model_training_config = config_manager.get_model_training_config()
        trainer = Training(config=model_training_config)
        trainer.get_base_model()
        trainer.train_valid_generator()
        trainer.train(callback_list=callbacks_list)


if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME_03} has started")
        model_training_pipeline = ModelTrainingPipeline()
        model_training_pipeline.forward()
        logger.info(f"{STAGE_NAME_03} has completed")
    except Exception as e:
        logger.exception(e)
        raise e
