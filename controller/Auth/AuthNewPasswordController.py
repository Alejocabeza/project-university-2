from controller.Controller import Controller
from modal.UserRepository import UserRepository


class AuthNewPasswordController(Controller):
    def __init__(self):
        super().__init__()
        self.user_repository = UserRepository()

    def new_password(self, data):
        user = self._current_user()

        if data.get("password") != data.get("confirmedPassword"):
            return "The passwords do not match"

        try:
            return self.user_repository.update(user.get("id"), data)
        except Exception as ex:
            print(f"Error al actualizar la contraseña el usuario: {ex}")
            return None
