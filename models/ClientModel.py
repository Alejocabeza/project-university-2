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
        return self._find_one_by({"id": id})