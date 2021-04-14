__version__ = "0.1.0"

import logging
import os
from pathlib import Path

import dotenv

dotenv.load_dotenv()

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.getLevelName(os.environ["LOG_LEVEL"]))

PROJECT_DIR = Path("..")
