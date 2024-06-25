from controller.Controller import Controller
from models.UserModel import UserModel


class FindUserByIdController(Controller):
    def __init__(self):
        super().__init__()
        self.user_repository = UserModel()

    def find_by_id(self, id):
        try:
            return self.user_repository.finder_user_by_id(id)
        except Exception as e:
            print(f"Cannot find user: {e}")
            return None
