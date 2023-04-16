import os

from dotenv import load_dotenv

load_dotenv('env.envs')
SQL_ECHO = bool(int(os.getenv('SQL_ECHO')))
POSTGRES_DB_URL = os.getenv('POSTGRES_DB_URL')
CACHE_TIME_TO_LIVE = int(os.getenv('CACHE_TIME_TO_LIVE'))