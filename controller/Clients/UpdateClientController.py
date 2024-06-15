from models.ClientModel import ClientModel
from controller.Controller import Controller


class UpdateClientController(Controller):
    def __init__(self):
        super().__init__()
        self.client_model = ClientModel()

    def update(self, id, data):
        try:
            data["updated_by"] = self._current_user().get("id")
            return self.client_model.client_update(id, data)
        except Exception as ex:
            print(f"Error al actualizar el client: {ex}")
            return None
