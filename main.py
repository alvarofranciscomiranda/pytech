from src.read_csv import run_function
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import os

engine = create_engine(os.getenv("DB_URI"))

def app():
    with engine.connect() as conn:
        stmt = text("select * from pg_database")
        print(conn.execute(stmt).fetchall())


if __name__ == "__main__":

    filename = 'resources/farm_data/farm1/minute_values.csv'
    app()
    #run_function()