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
        address_check = self._find_one_by({"name": data.get("name")})
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

    def remove_address(self, id):
        """
        Remove una dirección

        Args:
            id(int): el identificador de la dirección
        """
        return self._remove(id)

    def find_all_address(self):
        """
        Busca todas las direcciones
        """
        return self._find_all()
