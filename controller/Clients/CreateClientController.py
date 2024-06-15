from controller.Controller import Controller
from models.ClientModel import ClientModel


class CreateClientController(Controller):
    def __init__(self):
        super().__init__()
        self.client_model = ClientModel()

    def create(self, data):
        try:
            data["created_by"] = self._current_user().get("id")
            return self.client_model.client_create(data)
        except Exception as ex:
            print(f"Error al crear el client: {ex}")
            return None
