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