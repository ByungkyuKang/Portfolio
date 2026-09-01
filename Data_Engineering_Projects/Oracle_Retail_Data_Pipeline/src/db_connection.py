import os
import oracledb

from dotenv import load_dotenv
from pathlib import Path
from sqlalchemy import create_engine


BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH)

def connect_db():
    connection = oracledb.connect(
        user=os.getenv("ORACLE_USER"),
        password=os.getenv("ORACLE_PASSWORD"),
        host=os.getenv("ORACLE_HOST"),
        port=int(os.getenv("ORACLE_PORT")),
        service_name=os.getenv("ORACLE_SERVICE")
    )

    return connection


def create_db_engine():
    user = os.getenv("ORACLE_USER")
    password = os.getenv("ORACLE_PASSWORD")
    host = os.getenv("ORACLE_HOST")
    port = os.getenv("ORACLE_PORT")
    service = os.getenv("ORACLE_SERVICE")

    engine = create_engine(
        f"oracle+oracledb://{user}:{password}@{host}:{port}/?service_name={service}"
    )

    return engine