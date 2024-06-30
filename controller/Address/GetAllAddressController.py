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
            if self._current_user().get("role") == "admin":
                return self.address_model.find_all_address()
            else:
                return self.address_model.find_by_user(self._current_user().get("id"))
        except Exception as ex:
            print(f"Error al obtener todas las direcciones: {ex}")
            return None
