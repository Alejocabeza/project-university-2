from controller.Controller import Controller
from models.UserModel import UserModel


class AuthRegisterController(Controller):
    def __init__(self):
        super().__init__()
        self.user_repository = UserModel()

    def create(self, data):
        try:
            if data is not None:
                # print(data)
                return self.user_repository.register(data)
        except Exception as ex:
            print(f"Error al registrar el usuario: {ex}")
            return None
