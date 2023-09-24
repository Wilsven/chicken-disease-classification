from chicken_disease_classification import *
from chicken_disease_classification.components.evaluation import Evaluation
from chicken_disease_classification.config.configuration import ConfigurationManager

STAGE_NAME_04 = "Evaluation Pipeline"


class EvaluationPipeline:
    def __init__(self):
        pass

    def forward(self):
        config_manager = ConfigurationManager()
        evaluation_config = config_manager.get_evaluation_config()
        evaluation = Evaluation(config=evaluation_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME_04} has started")
        evaluation_pipeline = EvaluationPipeline()
        evaluation_pipeline.forward()
        logger.info(f"{STAGE_NAME_04} has completed")
    except Exception as e:
        logger.exception(e)
        raise e
