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
        user = self._find_one_by({"email": email})
        if user is None:
            return f"El usuario con el email {email} no existe"

        user_pass = user.get("password")

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
        user_check = self._find_one_by({"email": data.get("email")})
        if user_check is not None:
            return f"The user with email {data.get('email')} already exists"

        if data.get("password") != data.get("confirmedPassword"):
            return "The passwords do not match"

        data_to_insert = {
            "nombre": data.get("nombre"),
            "password": self._hash_password(data.get("password")),
            "cedula": None,
            "email": data.get("email"),
            "avatar": None,
            "rol": "user",
        }

        self._save(data_to_insert)

    def update(self, user_id, data):
        """
        Actualiza los datos de un usuario

        Args:
            user_id (_type_): el identificador del usuario
            data (_type_): la data del usuario que quiere actualizar
        """

        return self._update(user_id, data)

    def remove(self, user_id):
        """
        Elimina un Usuario

        Args:
            user_id(int): el identificador del usuario
        """
        return self._remove(user_id)

    def finder_user_by_id(self, user_id):
        """
        Busca un usuario por su id

        Args:
            user_id (int): el identificador del usuario

        Returns:
            None: si el usuario no existe
            user: el usuario si existe
        """
        return self._find_one_by({"id": user_id})

    def _hash_password(self, password):
        return self.bcrypt.hash(password)

    def _verify_password(self, password, hash_pass):
        return self.bcrypt.verify(password, hash_pass)
