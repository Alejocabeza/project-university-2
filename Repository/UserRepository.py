from passlib.hash import bcrypt
from Repository.BaseRepository import BaseRepository

class User (BaseRepository):
    def __init__(self):
        super().__init__('users')
        self.bcrypt = bcrypt

    def login(self, email, password, confirmedPassword):
        user = self.__findByEmail(email)
        userPass = user[5]
        userPass2 = user[6]
        print(user, userPass, userPass2)

        if user is None:
            return "El usuario con el email %s no existe" % email

        if(password != confirmedPassword):
            return "Las contraseñas no coinciden"

        checkPass = self.__verify_password(password, userPass)
        checkPass2 = self.__verify_password(confirmedPassword, userPass2)

        if checkPass is not True and checkPass2 is not True:
            return "La contraseña es incorrecta"

        return user

    def register(self, data):
        userCheck = self.__findByEmail(data['email'])
        if userCheck is not None:
            return "El usuario con el email %s ya existe" % data['email']

        data['password'] = self.__hash_password(data['password'])
        data['confirmedPassword'] = self.__hash_password(data['password'])
        data['role'] = 'admin'
        data['active'] = False

        res = self._save(data)
        return res

    def __findByEmail(self, email):
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

    def __hash_password(self, password):
        try:
            return self.bcrypt.hash(password)
        except:
            return False

    def __verify_password(self, password, hash):
        try:
            return self.bcrypt.verify(password, hash)
        except:
            return False

