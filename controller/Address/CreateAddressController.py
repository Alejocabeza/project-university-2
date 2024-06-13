from controller.Controller import Controller
from models.AddressModel import AddressModel


class CreateAddressController(Controller):
    def __init__(self):
        super().__init__()
        self.address_mode = AddressModel()

    def create(self, data):
        try:
            return self.address_mode.create_address(data)
        except Exception as ex:
            print(f"Error al crear la dirección: {ex}")
            return None
