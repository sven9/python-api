import logging
import os

import dotenv

dotenv.load_dotenv()

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.getLevelName(os.environ["LOG_LEVEL"]))
