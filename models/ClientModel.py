from models.BaseModel import BaseModel


class ClientModel(BaseModel):
    def __init__(self):
        super().__init__("client")

    def client_create(self, data):
        """
        Crea un nuevo cliente
        """
        return self._save(data)

    def client_update(self, id, data):
        """
        Actualiza un cliente
        """
        return self._update(id, data)

    def client_remove(self, id):
        """
        Elimina un Cliente
        """
        return self._remove(id)

    def clients_all(self):
        """
        Devuelve todos los usuarios
        """
        return self._find_all()

    def find_by_id(self, id):
        """
        Buscar un cliente por ID

        Args:
            id (int): El ID del cliente
        """
        return self._find_one_by({"id": id})

    def find_by_name(self, name):
        """
        Buscar un cliente por nombre

        Args:
            name (str): El nombre del cliente
        """
        return self._find_one_by({"name": name})

    def find_by_user(self, user_id):
        """
        Buscar un registro por el usuario

        Args:
            user_id (int): El identificador del usuario
        """
        return self._find_by({"created_by": user_id})
