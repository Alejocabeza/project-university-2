
from controller.Controller import Controller
from models.ClientModel import ClientModel

class FindClientByNameController(Controller):
    def __init__(self):
        super().__init__()
        self.client_repository = ClientModel()

    def find_by_name(self, name):
        try:
            return self.client_repository.find_by_name(name)
        except Exception as ex:
            print(f"Error al buscar el cliente: {ex}")
            return None
