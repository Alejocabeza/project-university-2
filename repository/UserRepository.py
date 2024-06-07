from passlib.hash import bcrypt
from repository.BaseRepository import BaseRepository


class UserRepository(BaseRepository):
    """
    Clase para el manejo de usuarios
    """
    def __init__(self):
        super().__init__("usuarios")
        self.bcrypt = bcrypt

    def login(self, email, password):
        """
            Permite al usuario iniciar sesión

            arguments:
                email (str): el correo del usuario
                password (str): la contraseña del usuario

            returns:
                None: si el usuario no existe o la contraseña es incorrecta
                user: el usuario si la contraseña es correcta
        """
        user = self._find_by_email(email)
        if user is None:
            return f"El usuario con el email {email} no existe"

        user_pass = user.get('password')

        if user is None:
            return f"El usuario con el email {email} no existe"

        # verificación de la contraseña
        check_pass = self._verify_password(password, user_pass)
        if check_pass is not True:
            return "La contraseña es incorrecta"

        return user

    def register(self, data):
        """
        Maneja el registro de un usuario

        Args:
            data (directory): el diccionario con los datos del usuario
        """
        user_check = self._find_by_email(data.get('email'))
        if user_check is not None:
            return f"The user with email {data.get('email')} already exists"

        if data.get('password') != data.get('confirmedPassword'):
            return "The passwords do not match"

        data_to_insert = {
            "nombre": data.get('nombre'),
            "password": self._hash_password(data.get('password')),
            'cedula': None,
            "email": data.get('email'),
            'avatar': None,
            'rol': 'user'
        }

        result = self._save(data_to_insert)
        return  result

    def _find_by_email(self, email):
        """
            Hace una consulta a la base de datos para obtener el usuario

            arguments:
                email (str): el correo del usuario

            returns:
                None: si el usuario no existe
                user: el usuario si existe
        """
        sql = "SELECT * FROM usuarios WHERE email = %s"
        cursor = self.connect.cursor(dictionary=True)
        cursor.execute(sql, (email,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def _hash_password(self, password):
        return self.bcrypt.hash(password)

    def _verify_password(self, password, hash_pass):
        return self.bcrypt.verify(password, hash_pass)
