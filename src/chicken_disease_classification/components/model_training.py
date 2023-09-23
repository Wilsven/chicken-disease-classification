from pathlib import Path

import tensorflow as tf

from chicken_disease_classification.entity.config_entity import TrainingConfig


class Training:
    def __init__(self, config: TrainingConfig):
        self.model_training_config = config

    def get_base_model(self):
        """Load the updated base model."""
        self.model = tf.keras.models.load_model(
            self.model_training_config.updated_base_model_path
        )

    def train_valid_generator(self):
        "Creates the training and validation generator."
        data_generator_kwargs = {"rescale": 1.0 / 255, "validation_split": 0.2}
        data_flow_kwargs = {
            "target_size": self.model_training_config.image_size[:-1],
            "batch_size": self.model_training_config.batch_size,
            "interpolation": "bilinear",
        }

        valid_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(
            **data_generator_kwargs
        )

        self.valid_generator = valid_data_generator.flow_from_directory(
            directory=self.model_training_config.training_data,
            subset="validation",
            shuffle=False,
            **data_flow_kwargs,
        )

        if self.model_training_config.augmentation:
            train_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **data_generator_kwargs,
            )
        else:
            train_data_generator = valid_data_generator

        self.train_generator = train_data_generator.flow_from_directory(
            directory=self.model_training_config.training_data,
            subset="training",
            shuffle=True,
            **data_flow_kwargs,
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        """Saves the model to a given path."""
        model.save(path)

    def train(self, callback_list: list):
        "Initiates model training and save fine-tuned model."
        self.steps_per_epoch = (
            self.train_generator.samples // self.train_generator.batch_size
        )
        self.validation_steps = (
            self.valid_generator.samples // self.valid_generator.batch_size
        )

        self.model.fit(
            self.train_generator,
            epochs=self.model_training_config.epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator,
            callbacks=callback_list,
        )

        self.save_model(
            path=self.model_training_config.trained_model_path, model=self.model
        )
