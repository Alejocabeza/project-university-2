from controller.Controller import Controller
from models.ClientOfficeModel import ClientOfficeModel

class RemoveClientOfficeController(Controller):
    def __init__(self):
        super().__init__()
        self.client_office_model = ClientOfficeModel()

    def remove(self, id):
        try:
            return self.client_office_model.remove_client_office(id)
        except Exception as ex:
            print(f"Error al borrar la sucursal: {ex}")
            return None