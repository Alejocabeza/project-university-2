from controller.Controller import Controller
from models.UserModel import UserModel

class FindAllUserController(Controller):
    def __init__(self):
        super().__init__()
        self.user_model = UserModel()

    def find_all(self):
        try:
            return self.user_model.find_all()
        except Exception as ex:
            print(f"Error al buscar todos los usuarios: {ex}")
            return None