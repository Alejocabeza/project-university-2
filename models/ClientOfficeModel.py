from models.BaseModel import BaseModel


class ClientOfficeModel(BaseModel):
    def __init__(self):
        super().__init__("client_office")

    def create_client_office(self, data):
        """
        Crea un nuevo registro

        Args:
            data (dict): el diccionario con los datos
        """
        return self._save(data)

    def update_client_office(self, id, data):
        """
        Actualizar una sucursal del cliente

        Args:
            data (dict): el diccionario con los datos
        """
        return self._update(id, data)

    def remove_client_office(self, id):
        """
        Eliminar una sucursal

        Args:
            id (int): El identificador de la sucursal
        """
        return self._remove(id)

    def find_all_client_office(self):
        """
        Busca todas las sucursales
        """
        return self._find_all()

    def find_by_id(self, id):
        """
        Buscar una sucursal por su id

        Args:
            id (int): El identificador de la sucursal
        """
        return self._find_one_by({"id": id})

    def find_by_name(self, name):
        """
        Buscar una sucursal por su nombre

        Args:
            name (str): Nombre de la sucursal
        """
        return self._find_one_by({"name": name})

    def find_by_user(self, user_id):
        """
        Buscar un registro por el usuario

        Args:
            user_id (int): El identificador del usuario
        """
        return self._find_by({"created_by": user_id})
