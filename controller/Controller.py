from repository.UserRepository import UserRepository;
from repository.SessionRepository import SessionRepository;

class Controller:
    def __init__(self):
        self.user_repository = UserRepository()
        self.session_repository = SessionRepository()

    def _current_session(self):
        try:
            return self.session_repository.find_session_by_active()
        except Exception as ex:
            print(f"Error al obtener la sesión actual: {ex}")
            return None

    def _current_user(self):
        try:
            return self.user_repository.finder_user_by_id(self._current_session().get("usuario_id"))
        except Exception as ex:
            print(f"Error al obtener el usuario actual: {ex}")
            return None