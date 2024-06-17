from controller.Controller import Controller
from models.ClientOfficeModel import ClientOfficeModel

class GetAllClientOfficeController(Controller):
    def __init__(self):
        super().__init__()
        self.client_office_model = ClientOfficeModel()

    def find_all(self):
        try:
            return self.client_office_model.find_all_client_office()
        except Exception as ex:
            print(f"Error al optener todas las sucursales: {ex}")
            return None