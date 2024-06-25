from controller.Controller import Controller
from models.AddressModel import AddressModel


class GetAllAddressController(Controller):
    def __init__(self):
        super().__init__()
        self.address_model = AddressModel()

    def find_all(self):
        """
        Busca todas las direcciones

        Returns:
            list: Lista con las direcciones
        """
        try:
            return self.address_model.find_all_address()
        except Exception as ex:
            print(f"Error al obtener todas las direcciones: {ex}")
            return None
