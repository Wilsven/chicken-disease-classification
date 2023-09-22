import logging
import os
import sys
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOGS_PATH = os.path.join(os.getcwd(), "logs")
LOG_FILE_PATH = os.path.join(LOGS_PATH, LOG_FILE)


os.makedirs(LOGS_PATH, exist_ok=True)

if not os.path.exists(os.path.join(LOGS_PATH, ".gitkeep")):
    with open(os.path.join(LOGS_PATH, ".gitkeep"), "w") as f:
        pass

logging.basicConfig(
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(module)s %(name)s -  %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout),
    ],
)

logger = logging.getLogger("chicken-disease-logger")
