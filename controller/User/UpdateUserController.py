from models.UserModel import UserModel
from controller.Controller import Controller


class UpdateUserController(Controller):
    def __init__(self):
        super().__init__()
        self.user_model = UserModel()

    def update(self, id, data):
        try:
            if data is not None:
                return self.user_model.update(id, data)
        except Exception as ex:
            print(f"Error al actualizar el usuario: {ex}")
            return None
