from controller.Controller import Controller
from models.AddressModel import AddressModel


class RemoveAddressController(Controller):
    def __init__(self):
        super().__init__()
        self.address_model = AddressModel()

    def remove(self, id):
        try:
            return self.address_model.remove_address(id)
        except Exception as ex:
            print(f"Error al eliminar la dirección: {ex}")
            return None
