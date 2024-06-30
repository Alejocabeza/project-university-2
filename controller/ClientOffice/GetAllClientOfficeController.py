from controller.Controller import Controller
from models.ClientOfficeModel import ClientOfficeModel


class GetAllClientOfficeController(Controller):
    def __init__(self):
        super().__init__()
        self.client_office_model = ClientOfficeModel()

    def find_all(self):
        try:
            if self._current_user().get("role") == "admin":
                return self.client_office_model.find_all_client_office()
            else:
                return self.client_office_model.find_by_user(
                    self._current_user().get("id")
                )
        except Exception as ex:
            print(f"Error al optener todas las sucursales: {ex}")
            return None
