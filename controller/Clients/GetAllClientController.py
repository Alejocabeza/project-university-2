from controller.Controller import Controller
from models.ClientModel import ClientModel


class GetAllClientController(Controller):
    def __init__(self):
        super().__init__()
        self.client_model = ClientModel()

    def find_all(self):
        try:
            return self.client_model.clients_all()
        except Exception as ex:
            print(f"Error al optener todos los clientes: {ex}")
            return None
