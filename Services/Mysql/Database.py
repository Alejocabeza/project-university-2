import mysql.connector as mysql

def db():
    return mysql.connect(
        host="localhost",
        user="root",
        passwd="",
        database="university"
    )
