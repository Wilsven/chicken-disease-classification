from pathlib import Path
import tensorflow as tf
from chicken_disease_classification.entity.config_entity import EvaluationConfig
from chicken_disease_classification.utils.common import save_json


class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.evaluation_config = config

    def _eval_valid_generator(self):
        data_generator_kwargs = {"rescale": 1.0 / 255, "validation_split": 0.3}
        data_flow_kwargs = {
            "target_size": self.evaluation_config.image_size[:-1],
            "batch_size": self.evaluation_config.batch_size,
            "interpolation": "bilinear",
        }

        valid_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(
            **data_generator_kwargs
        )

        self.valid_generator = valid_data_generator.flow_from_directory(
            directory=self.evaluation_config.training_data,
            subset="validation",
            shuffle=False,
            **data_flow_kwargs,
        )

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)

    def evaluation(self):
        model = self.load_model(self.evaluation_config.path_to_model)
        self._eval_valid_generator()
        self.score = model.evaluate(self.valid_generator)

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)
