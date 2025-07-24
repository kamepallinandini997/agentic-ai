import logging
from logging.handlers import RotatingFileHandler
import os

# Create logs directory if doesn't exist
LOG_dir = "logs"
os.makedirs(LOG_dir, exist_ok= True)

# Define log path
LOG_FILE = os.path.join(LOG_dir,"users.log")

log_format = "%(asctime)s - %(levelname)s - %(filename)s - %(message)s"
formatter = logging.Formatter(log_format)

# Setting up rotating file handler max size = 1 MB and keep 2 backupcounts
file_handler = RotatingFileHandler(LOG_FILE,maxBytes=1_00_00, backupCount=2)
file_handler.setFormatter(formatter)

# Step 5: Get the logger
logger = logging.getLogger("user_registration")
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
