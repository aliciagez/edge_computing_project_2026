import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
HOST = os.getenv("DB_HOST", "localhost")

DB_CONFIG = f"dbname={POSTGRES_DB} user={POSTGRES_USER} password={POSTGRES_PASSWORD} host={HOST}"

def query_db(sql, parameters: tuple = None):
    with psycopg2.connect(DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parameters)
            return cur.fetchall() if cur.description else None