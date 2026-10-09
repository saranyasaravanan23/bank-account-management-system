
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

def create_connection():
    print("Trying to connect to MySQL...", flush=True)

    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "127.0.0.1"),
            port=3306,
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME", "bank_management_db"),
            connection_timeout=5,
            use_pure=True
        )

        print("MySQL connection successful!", flush=True)
        return connection

    except Exception as e:
        print("MySQL connection failed!", flush=True)
        print("Error:", repr(e), flush=True)
        return None
