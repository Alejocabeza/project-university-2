from controller.Controller import Controller
from models.AddressModel import AddressModel


class FindAddressByNameController(Controller):
    def __init__(self):
        super().__init__()
        self.address_repository = AddressModel()

    def find_by_name(self, name):
        """
        Buscar una dirección por su nombre

        Args:
            name (str): El nombre de la dirección
        """
        try:
            return self.address_repository.find_by_name(name)
        except Exception as ex:
            print(f"Error al buscar la dirección: {ex}")
            return None
