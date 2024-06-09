from controller.Controller import Controller
from repository.UserRepository import UserRepository

class AuthLoginController(Controller):
    def __init__(self):
        super().__init__()
        self.user_repository = UserRepository()

    def login(self, email, password):
        try:
            return self.user_repository.login(email, password)
        except Exception as ex:
            print(f"Error al iniciar sesión: {ex}")
            return None