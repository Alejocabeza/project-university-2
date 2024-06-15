from datetime import datetime
from models.UserModel import UserModel
from models.SessionModel import SessionModel


class Controller:
    def __init__(self):
        self.user_repository = UserModel()
        self.session_repository = SessionModel()

    def _current_session(self):
        try:
            return self.session_repository.find_session_by_active()
        except Exception as ex:
            print(f"Error al obtener la sesión actual: {ex}")
            return None

    def _current_user(self):
        try:
            return self.user_repository.finder_user_by_id(
                self._current_session().get("user")
            )
        except Exception as ex:
            print(f"Error al obtener el usuario actual: {ex}")
            return None

    def _current_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
