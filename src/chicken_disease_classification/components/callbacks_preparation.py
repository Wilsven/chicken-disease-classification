import os
import time
import tensorflow as tf

from chicken_disease_classification.entity.config_entity import CallbacksConfig


class Callbacks:
    def __init__(self, config: CallbacksConfig):
        self.callbacks_config = config

    @property
    def _create_tb_callbacks(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir = os.path.join(
            self.callbacks_config.tensorboard_log_dir, f"tb_logs_at_{timestamp}"
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)

    @property
    def _create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=str(self.callbacks_config.checkpoints_file_path),
            save_best_only=True,
        )

    def get_tb_ckpt_callbacks(self):
        return [self._create_tb_callbacks, self._create_ckpt_callbacks]
