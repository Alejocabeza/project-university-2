from services.Database import db
from passlib.hash import bcrypt

class User ():
    def __init__(self):
        self.connect = db()
        self.cursor = self.connect.cursor()
        self.bcrypt = bcrypt

    def findAll(self):
        try:
            sql = "SELECT * FROM users"
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as ex:
            print("Error al ejecutar la consulta %s" % ex)
            return None
        finally:
            self.cursor.close()
            self.connect.close()

    def login(self, email, password, confirmedPassword):
        user = self._findByEmail(email)
        userPass = user[5]
        userPass2 = user[6]
        print(user, userPass, userPass2)

        if user is None:
            return "El usuario con el email %s no existe" % email

        if(password != confirmedPassword):
            return "Las contraseñas no coinciden"

        checkPass = self._verify_password(password, userPass)
        checkPass2 = self._verify_password(confirmedPassword, userPass2)

        if checkPass is not True and checkPass2 is not True:
            return "La contraseña es incorrecta"

        return user

    def _findByEmail(self, email):
        try:
            sql = "SELECT * FROM users WHERE email = %s"
            self.cursor.execute(sql, (email,))
            return self.cursor.fetchone()
        except Exception as ex:
            print("Error al ejecutar la consulta %s" % ex)
            return None
        finally:
            self.cursor.close()
            self.connect.close()

    def _hash_password(self, password):
        try:
            return self.bcrypt.hash(password)
        except:
            return False

    def _verify_password(self, password, hash):
        try:
            return self.bcrypt.verify(password, hash)
        except:
            return False

