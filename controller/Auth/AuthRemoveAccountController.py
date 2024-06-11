from controller.Controller import Controller
from models.UserModel import UserModel


class AuthRemoveAccountController(Controller):
    def __init__(self):
        super().__init__()
        self.user_repository = UserModel()

    def remove_account(self):
        user = self._current_user()
        try:
            self.user_repository.remove(user.get("id"))
        except Exception as e:
            print(f"Error al eliminar el usuario: {e}")
            return None
