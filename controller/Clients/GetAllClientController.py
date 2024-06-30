from controller.Controller import Controller
from models.ClientModel import ClientModel


class GetAllClientController(Controller):
    def __init__(self):
        super().__init__()
        self.client_model = ClientModel()

    def find_all(self):
        try:
            if self._current_user().get("role") == "admin":
                return self.client_model.clients_all()
            else:
                return self.client_model.find_by_user(self._current_user().get("id"))
        except Exception as ex:
            print(f"Error al optener todos los clientes: {ex}")
            return None
