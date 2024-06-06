import mysql.connector as MySQL


def db():
    db = MySQL.connect(
        host="localhost", user="root", passwd="root", database="proyecto_universidad"
    )
    return db.cursor()

