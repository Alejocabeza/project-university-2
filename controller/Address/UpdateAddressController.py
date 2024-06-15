from controller.Controller import Controller
from models.AddressModel import AddressModel


class UpdateAddressController(Controller):
    def __init__(self):
        super().__init__()
        self.address_mode = AddressModel()

    def update(self, id, data):
        try:
            data['updated_by'] = self._current_user().get('id')
            return self.address_mode.update_address(id, data)
        except Exception as ex:
            print(f"Error al crear la dirección: {ex}")
            return None
