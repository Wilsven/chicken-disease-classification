import os
from pathlib import Path

from logger import logging

PROJECT_NAME = "chicken_disease_classification"

FILE_PATHS = [
    ".github/workflows/.gitkeep",
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/config/configuration.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/constants/__init__.py",
    "config/config.yaml",
    "main.py",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

for file_path in FILE_PATHS:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if len(file_dir) != 0:
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir}")

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, "w") as f:
            logging.info(f"Creating file: {file_name}")
            pass

    else:
        logging.info(
            f"File {file_name} already exists in file directory/path {file_dir}"
        )
