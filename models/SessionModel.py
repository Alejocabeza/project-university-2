from datetime import datetime
from models.BaseModel import BaseModel


class SessionModel(BaseModel):
    """
    Clase para el manejar las sesiones del usuario
    """

    def __init__(self):
        super().__init__("user_session")

    def create_session(self, id):
        """
        Crea una nueva sesión

        Args:
            user (Usuario): el usuario que inicia la sesión
        """
        check_session = self._find_by({"is_active": True})
        if check_session is not None:
            for session in check_session:
                self.close_session(session.get("id"))

        data_to_insert = {
            "user": id,
            "startDate": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "endDate": None,
            "is_active": True,
        }

        self._save(data_to_insert)

    def close_session(self, session_id):
        """
        Cambia el estado de una sesión
        Args:
            session_id (int): el identificador de la sesión
        """

        data_to_update = {
            "endDate": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "is_active": False,
        }

        self._update(session_id, data_to_update)

    def find_session_by_active(self):
        """
        Busca una sesión activa
        """
        return self._find_one_by({"is_active": True})
