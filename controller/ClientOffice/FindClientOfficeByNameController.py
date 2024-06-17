from models.ClientOfficeModel import ClientOfficeModel
from controller.Controller import Controller

class FindClientOfficeByNameController(Controller):
    def __init__(self):
        super().__init__()
        self.client_office_repository = ClientOfficeModel()

    def find_by_name(self, name):
        try:
            return self.client_office_repository.find_by_name(name)
        except Exception as ex:
            print(f"Error al buscar la sucursal: {ex}")
            return None