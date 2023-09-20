import logging
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOGS_PATH = os.path.join(os.getcwd(), "logs")
LOG_FILE_PATH = os.path.join(LOGS_PATH, LOG_FILE)


os.makedirs(LOGS_PATH, exist_ok=True)

if not os.path.exists(os.path.join(LOGS_PATH, ".gitkeep")):
    with open(os.path.join(LOGS_PATH, ".gitkeep"), "w") as f:
        pass

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s -  %(levelname)s - %(message)s",
)
