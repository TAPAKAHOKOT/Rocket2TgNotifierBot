from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
import logging

load_dotenv()
logging.info('Loaded dotenv')

class Settings:
    def __init__(self):
        self.is_testing = getenv('TESTING_MODE') == 'TRUE'
        logging.info(f'Is testing = {self.is_testing}')

        self.token = getenv('TEST_BOT_TOKEN') if self.is_testing else getenv('BOT_TOKEN')
        self.admins = getenv('ADMINS').split(',')
        logging.info(f'Admins = {self.admins}')

        logging.info('Loaded .env variables')

        self.bot = Bot(token=self.token)
        logging.info('Created Bot')
        
        self.dp = Dispatcher(self.bot)
        logging.info('Created Dispatcher')