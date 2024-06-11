from controller.Controller import Controller
from models.SessionModel import SessionModel


class AuthCloseSessionController(Controller):
    def __init__(self):
        super().__init__()
        self.session_repository = SessionModel()

    def close_session(self):
        try:
            return self.session_repository.close_session(
                self._current_session().get("id")
            )
        except Exception as ex:
            print(f"Error al cerrar la sesión: {ex}")
            return None
