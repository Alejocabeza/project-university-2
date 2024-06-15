from models.AddressModel import AddressModel
from controller.Controller import Controller


class FindAddressByIdController(Controller):
    def __init__(self):
        super().__init__()
        self.address_repository = AddressModel()

    def find_by_id(self, id):
        """
        Busca una dirección por su identificador
        """
        try:
            return self.address_repository.find_by_id(id)
        except Exception as ex:
            print(f"Error al buscar la dirección: {ex}")
            return None
