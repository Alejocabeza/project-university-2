from controller.Controller import Controller
from modal.SessionRepository import SessionRepository


class AuthCreateSessionController(Controller):
    def __init__(self):
        super().__init__()
        self.session_repository = SessionRepository()

    def new_session(self, user_id):
        try:
            return self.session_repository.create_session(user_id)
        except Exception as ex:
            print(f"Error al crear la sesión: {ex}")
            return None
