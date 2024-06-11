from controller.Controller import Controller
from models.UserModel import UserModel


class AuthLoginController(Controller):
    def __init__(self):
        super().__init__()
        self.user_repository = UserModel()

    def login(self, email, password):
        try:
            return self.user_repository.login(email, password)
        except Exception as ex:
            print(f"Error al iniciar sesión: {ex}")
            return None
