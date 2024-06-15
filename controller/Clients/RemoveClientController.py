from controller.Controller import Controller
from models.ClientModel import ClientModel


class RemoveClientController(Controller):
    def __init__(self):
        super().__init__()
        self.client_model = ClientModel()

    def remove(self, id):
        try:
            return self.client_model.client_update(
                id, {"deleted_at": self._current_time()}
            )
        except Exception as ex:
            print(f"Error al eliminar el cliente: {ex}")
            return None
