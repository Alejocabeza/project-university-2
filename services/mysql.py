import os
import mysql.connector as mysql
from dotenv import load_dotenv

load_dotenv()

db = mysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
)
