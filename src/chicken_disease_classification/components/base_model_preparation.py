from pathlib import Path
from typing import Optional

import tensorflow as tf

from chicken_disease_classification.entity.config_entity import BaseModelConfig


class BaseModel:
    def __init__(self, config: BaseModelConfig):
        self.base_model_config = config

    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.base_model_config.image_size,
            weights=self.base_model_config.weights,
            include_top=self.base_model_config.include_top,
        )

        self.save_model(path=self.base_model_config.base_model_path, model=self.model)

    @staticmethod
    def _prepare_full_model(
        model: tf.keras.Model,
        classes: int,
        learning_rate: float,
        freeze_all: Optional[bool] = True,
        freeze_till: Optional[int] = None,
    ):
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                layer.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation="softmax",
        )(flatten_in)

        full_model = tf.keras.models.Model(
            inputs=model.output,
            outputs=prediction,
        )

        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"],
        )

        full_model.summary()

        return full_model

    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.base_model_config.classes,
            learning_rate=self.base_model_config.learning_rate,
            freeze_all=True,
            freeze_till=None,
        )

        self.save_model(
            path=self.base_model_config.updated_base_model_path, model=self.full_model
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
