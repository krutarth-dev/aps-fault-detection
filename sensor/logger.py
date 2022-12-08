import logging
import os
from datetime import datetime
import os

#log file name
LOG_FILE_NAME = f"{atetime.now().strftime('%m%d%y__%H_%M_%S')}.log"

#log directory
LOG_FILE_DIR = os.path.join(os.getcwd(),"logs")

#create folder if not avialable
os.makedirs(LOG_FILE_DIR,exist_ok=True)

#log file path
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)