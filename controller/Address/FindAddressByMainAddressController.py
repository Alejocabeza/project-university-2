from models.AddressModel import AddressModel
from controller.Controller import Controller

class FindAddressByMainAddressController(Controller):
    def __init__(self):
        super().__init__()
        self.address_model = AddressModel()

    def find_by_main_address(self, main_address):
        try:
            return self.address_model.find_by_main_address(main_address)
        except Exception as ex:
            print(f"Error al optener todas las direcciones: {ex}")
            return None
