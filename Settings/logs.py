import logging
from os import mkdir

try: mkdir("Logs")
except FileExistsError: pass

logging.basicConfig(
    level=logging.DEBUG, 
    handlers=(
        logging.FileHandler('Logs/logs.log', mode='a'), 
        logging.StreamHandler()
    ),
    format='[%(asctime)s %(levelname)s] %(message)s',
    datefmt='%d.%m.%Y %H:%M:%S'
)

logging.info('-'*50)
logging.info('Logging start')