from controller.Controller import Controller
from models.AddressModel import AddressModel


class CreateAddressController(Controller):
    """
    Crea una dirección
    """
    def __init__(self):
        super().__init__()
        self.address_mode = AddressModel()

    def create(self, data):
        """
        Crea una dirección

        Args:
            data (dict): Diccionario con los datos

        Returns:
            True: True si la dirección se crea correctamente
            False: False si la dirección no se crea correctamente
        """
        try:
            data['main_address'] = f"{data.get('department')} {data.get('street')} {data.get('location')} {data.get('state')} {data.get('country')} {data.get('postal_code')}"
            data['created_by'] = self._current_user().get('id')
            return self.address_mode.create_address(data)
        except Exception as ex:
            print(f"Error al crear la dirección: {ex}")
            return None
