from controller.Controller import Controller
from models.UserModel import UserModel


class AuthRegisterController(Controller):
    def __init__(self):
        super().__init__()
        self.user_repository = UserModel()

    def register(self, data):
        try:
            return self.user_repository.register(data)
        except Exception as ex:
            print(f"Error al registrar el usuario: {ex}")
            return None
