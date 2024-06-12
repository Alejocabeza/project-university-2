from models.UserModel import UserModel
from controller.Controller import Controller


class RemoveUserController(Controller):
    def __init__(self):
        super().__init__()
        self.user_model = UserModel()

    def remove(self, id):
        try:
            self.user_model.remove(id)
        except Exception as ex:
            print(f"Error al borrar al usuario: {ex}")
            return None
