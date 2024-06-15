from controller.Controller import Controller
from models.AddressModel import AddressModel


class RemoveAddressController(Controller):
    def __init__(self):
        super().__init__()
        self.address_model = AddressModel()

    def remove(self, id):
        try:
            return self.address_model.update_address(id, {"deleted_at": self._current_time()})
        except Exception as ex:
            print(f"Error al eliminar la dirección: {ex}")
            return None
