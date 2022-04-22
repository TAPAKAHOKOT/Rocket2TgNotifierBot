import logging
from os import mkdir
from dotenv import load_dotenv
from os import getenv

load_dotenv()

try: mkdir("Logs")
except FileExistsError: pass

env_logging_level = getenv('LOGGING_LEVEL')
logging_level = logging.INFO
if env_logging_level == 'INFO':
    logging_level = logging.INFO
elif env_logging_level == 'DEBUG':
    logging_level = logging.DEBUG

logging.basicConfig(
    level=logging_level,
    handlers=(
        logging.FileHandler('Logs/logs.log', mode='a'), 
        logging.StreamHandler()
    ),
    format='[%(asctime)s %(levelname)s] %(message)s',
    datefmt='%d.%m.%Y %H:%M:%S'
)

logging.info('-'*50)
logging.info('Logging start')