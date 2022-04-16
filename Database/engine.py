from sqlalchemy import create_engine
from os import getenv
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(
    '{DB_NAME}://{DB_USER}:{DB_PASS}@{DB_HOST}/{TABLE_NAME}'.format(
        DB_NAME=getenv("DB_NAME"),
        DB_USER=getenv("DB_USER"),
        DB_PASS=getenv("DB_PASS"),
        DB_HOST=getenv("DB_HOST"),
        TABLE_NAME=getenv("TABLE_NAME")
    ), echo=True
)