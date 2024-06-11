from controller.Controller import Controller
from models.UserModel import UserModel


class AuthUpdateController(Controller):
    def __init__(self):
        super().__init__()
        self.user_repository = UserModel()

    def update(self, data):
        user = self._current_user()
        print(data)
        if data:
            try:
                return self.user_repository.update(user.get("id"), data)
            except Exception as ex:
                print(f"Error al actualizar el usuario: {ex}")
                return None
