from models.BaseModel import BaseModel

class AddressModel(BaseModel):
    """
    Clase para las direcciones
    """

    def __init__(self):
        super().__init__("address")

    def create_address(self, data):
        """
        Crear una dirección

        Args:
            data (directory): el diccionario con los datos de la dirección

        Returns:
            Boolean: True si la dirección se crea correctamente
        """
        address_check = self._find_one_by(
            {"name": data.get("name"), "deleted_at": None}
        )
        if address_check is not None:
            return f"La dirección con el nombre {data.get('name')} ya existe"

        return self._save(data)

    def update_address(self, id, data):
        """
        Actualizar una dirección

        Args:
            id(int): el identificador de la dirección
            data(directory): el diccionario con los datos de la dirección
        """
        return self._update(id, data)

    def find_all_address(self):
        """
        Busca todas las direcciones
        """
        return self._find_all()

    def find_by_main_address(self, main_address):
        """
        Busca la dirección por la dirección principal
        """
        return self._find_one_by({"main_address": main_address, "deleted_at": None})

    def find_by_id(self, id):
        """
        Buscar una dirección por su identificador

        Args:
            id (int): El identificador de la dirección
        """
        return self._find_one_by({"id": id})

    def find_by_name(self, name):
        """
        Buscar una dirección por su nombre

        Args:
            name (str): El nombre de la dirección
        """
        return self._find_one_by({"name": name})
