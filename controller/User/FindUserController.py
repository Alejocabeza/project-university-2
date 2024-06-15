from models.UserModel import UserModel
from controller.Controller import Controller

class FindUserController(Controller):
    """
    Controller para buscar un usuario por el ID

    Args:
        Controller (Controller): Clase principal del controlador
    """
    def __init__(self):
        super().__init__()
        self.user_model = UserModel()

    def find_user(self, user_id):
        """
        Busca un usuario por el ID

        Args:
            user_id (int): Identificador del usuario

        Returns:
            User: El usuario encontrado
            None: Si el usuario no existe
        """
        try:
            return self.user_model.finder_user_by_id(user_id)
        except Exception as ex:
            print(f"Error al buscar el usuario: {ex}")
            return None