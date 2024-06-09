from controller.Controller import Controller
from modal.UserRepository import UserRepository


class AuthRemoveAccountController(Controller):
    def __init__(self):
        super().__init__()
        self.user_repository = UserRepository()

    def remove_account(self):
        user = self._current_user()
        try:
            self.user_repository.remove(user.get("id"))
        except Exception as e:
            print(f"Error al eliminar el usuario: {e}")
            return None
