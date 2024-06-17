from controller.Controller import Controller
from models.ClientOfficeModel import ClientOfficeModel

class UpdateClientOfficeController(Controller):
    def __init__(self):
        super().__init__()
        self.client_office_model = ClientOfficeModel()

    def update(self, id, data):
        try:
            data['updated_by'] = self._current_user().get('id')
            return self.client_office_model.update_client_office(id, data)
        except Exception as ex:
            print(f"Error al actualizar la sucursal: {ex}")
            return None
