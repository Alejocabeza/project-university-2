
from controller.Controller import Controller
from models.ClientModel import ClientModel

class FindClientByIdController(Controller):
    def __init__(self):
        super().__init__()
        self.client_repository = ClientModel()

    def find_by_id(self, id):
        try:
            return self.client_repository.find_by_id(id)
        except Exception as ex:
            print(f"Cannot find client by id: {ex}")
            return None
