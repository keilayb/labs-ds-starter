"""Database functions"""

import os
from dotenv import load_dotenv
from fastapi import APIRouter, Depends
import sqlalchemy
import pandas as pd

router = APIRouter()


async def get_db() -> sqlalchemy.engine.base.Connection:
    """Get a SQLAlchemy database connection.

    Uses this environment variable if it exists:  
    DATABASE_URL=dialect://user:password@host/dbname

    Otherwise uses a SQLite database for initial local development.
    """
    load_dotenv()
    database_url = os.getenv('DATABASE_URL', default='sqlite:///temporary.db')
    engine = sqlalchemy.create_engine(database_url)
    connection = engine.connect()
    try:
        yield connection
    finally:
        connection.close()


@router.get('/info')
async def get_url(connection=Depends(get_db)):
    """Verify we can connect to the database, 
    and return the database URL in this format:

    dialect://user:password@host/dbname

    The password will be hidden with *** 🤫
    """
    url_without_password = repr(connection.engine.url)
    return {'database_url': url_without_password}


@router.get('/write_data')
async def write_data(df, connection=Depends(get_db)):
    tablename = 'mytable'
    df = pd.util.testing.makeDataFrame()
    df.to_sql(tablename, connection, if_exists='append',
              index=False, method='multi')
    return f"Data written to table named {tablename}"


@router.get('/read_data')
async def read_data(connection=Depends(get_db)):
    query = """SELECT * FROM mytable LIMIT 5"""
    df = pd.read_sql(query, connection)
    return df.to_dict(orient='records')
