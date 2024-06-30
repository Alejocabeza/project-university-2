from passlib.hash import bcrypt
from models.BaseModel import BaseModel


class UserModel(BaseModel):
    """
    Clase para el manejo de usuarios
    """

    def __init__(self):
        super().__init__("user")
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

        pass_hash = self._hash_password(data.get("password"))
        data["password"] = pass_hash

        return self._save(data)

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

    def find_all(self):
        """
        Devuelve todos los usuarios
        """
        return self._find_all()

    def _hash_password(self, password):
        """
        Este metodo encripta la contraseña del usuario
        """
        return self.bcrypt.hash(password)

    def _verify_password(self, password, hash_pass):
        """
        Este Metodo verifica la contraseña encripta al momento del login
        """
        return self.bcrypt.verify(password, hash_pass)

    def find_by_user(self, user_id):
        """
        Buscar un registro por el usuario

        Args:
            user_id (int): El identificador del usuario
        """
        return self._find_by({"created_by": user_id})
