from controller.Controller import Controller
from modal.UserRepository import UserRepository


class AuthRegisterController(Controller):
    def __init__(self):
        super().__init__()
        self.user_repository = UserRepository()

    def register(self, data):
        try:
            return self.user_repository.register(data)
        except Exception as ex:
            print(f"Error al registrar el usuario: {ex}")
            return None
