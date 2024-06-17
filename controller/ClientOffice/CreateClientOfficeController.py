from controller.Controller import Controller
from models.ClientOfficeModel import ClientOfficeModel

class CreateClientOfficeController(Controller):
    def __init__(self):
        super().__init__()
        self.client_office_model = ClientOfficeModel()

    def create(self, data):
        try:
            data['created_by'] = self._current_user().get('id')
            self.client_office_model.create_client_office(data)
        except Exception as ex:
            print(f"Error al crear la sucursal: {ex}")
            return None