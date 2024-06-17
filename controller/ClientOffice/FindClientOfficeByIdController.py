from models.ClientOfficeModel import ClientOfficeModel
from controller.Controller import Controller


class FindClientOfficeByIdController(Controller):
    def __init__(self):
        super().__init__()
        self.clinet_office_repository = ClientOfficeModel()

    def find_by_id(self, id):
        """
        Busca una dirección por su identificador
        """
        try:
            return self.clinet_office_repository.find_by_id(id)
        except Exception as ex:
            print(f"Error al buscar la dirección: {ex}")
            return None
