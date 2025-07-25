# Import necessary modules here

import logging
from logging.handlers import RotatingFileHandler
import os

#  Create logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

#  Defining log file path
LOG_FILE = os.path.join(LOG_DIR, "users.log")

# Defining log format
log_format = '%(asctime)s - %(levelname)s - %(filename)s - %(message)s'
formatter = logging.Formatter(log_format)

#  Setting up a rotating file handler with max size  1MB and  keep 3 backups)
file_handler = RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=3)
file_handler.setFormatter(formatter)

# Get the logger
logger = logging.getLogger("user_registration")
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
