import os
import logging
import sys


logging_string = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

logging_dir = "logs"
logging_path = os.path.join(logging_dir, 'running_logs.log')
os.makedirs(logging_dir, exist_ok=True)


logging.basicConfig(
    level=logging.INFO, 
    format=logging_string, 

    handlers = [
        logging.FileHandler(logging_path), 
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("mlProjectLogger")
