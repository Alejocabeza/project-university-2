from controller.Controller import Controller


class GetUserController(Controller):
    def __init__(self):
        super().__init__()

    def get_user_data(self):
        try:
            return self._current_user()
        except Exception as ex:
            print(f"Error al optener la información del usuario: {ex}")
            return None
