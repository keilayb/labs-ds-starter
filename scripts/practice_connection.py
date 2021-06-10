"""Practice setting up connection to database"""

import os
from dotenv import load_dotenv
import sqlalchemy

load_dotenv()

master_username = os.getenv('master_username')
master_password = os.getenv('master_password')
endpoint = os.getenv('endpoint')

database_url = f'postgresql://{master_username}:{master_password}@{endpoint}'

engine = sqlalchemy.create_engine(database_url)
connection = engine.connect()
