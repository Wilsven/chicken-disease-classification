import base64
import json
import os
from pathlib import Path
from typing import Any

import joblib
import yaml
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations

from chicken_disease_classification import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads YAML file and returns key value pairs as class attributes.

    Args:
        path_to_yaml (Path): Path to load YAML file from.

    Raises:
        ValueError: Raises error if YAML file is empty.
        e: Raises error.

    Returns:
        ConfigBox: Data loaded as class attributes.
    """
    try:
        with open(path_to_yaml) as f:
            content = yaml.safe_load(f)
            logger.info(f"Loaded YAML file successfully from: {path_to_yaml}")

            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    """Creates directories from a list of paths.

    Args:
        path_to_directories (list[Path]): A list of paths.
        verbose (bool, optional): If True, logs the process. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves data as a JSON file.

    Args:
        path (Path): A path to save the JSON file to.
        data (dict): Data to save as a JSON.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"JSON file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads JSON file data.

    Args:
        path (Path): Path to load JSON file from.

    Returns:
        ConfigBox: Data loaded as class attributes instead of dictionary.
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"JSON file loaded succesfully from: {path}")

    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves binary file.

    Args:
        data (Any): Data to be saved as binary.
        path (Path): Path to save data as binary to.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads binary data.

    Args:
        path (Path): Path to load binary data from.

    Returns:
        Any: Returns data.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")

    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """Get size in KB.

    Args:
        path (Path): Path of the file to get size of.

    Returns:
        str: Size in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)

    return f"~ {size_in_kb} KB"


def decode_image(img_str: str, file_name: Path):
    img_data = base64.b64decode(img_str)
    with open(file_name, "wb") as f:
        f.write(img_data)
        f.close()


def encode_image_into_base64(cropped_image_path: Path) -> str:
    with open(cropped_image_path, "rb") as f:
        return base64.b64encode(f.read())
