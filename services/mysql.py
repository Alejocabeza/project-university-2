import mysql.connector as mysql


def db():
    return mysql.connect(
        host="localhost", user="root", passwd="root", database="proyecto_universidad"
    )
