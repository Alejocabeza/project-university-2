from repository.BaseRepository import BaseRepository
from datetime import datetime


class SessionRepository(BaseRepository):
    """
    Clase para el manejar las sesiones del usuario
    """

    def __init__(self):
        super().__init__("sesiones_de_usuarios")

    def create_session(self, id):
        """
        Crea una nueva sesión

        Args:
            user (Usuario): el usuario que inicia la sesión
        """
        check_session = self._find_by({"estado": True})
        if check_session is not None:
            for session in check_session:
                self.close_session(session.get("id"))

        data_to_insert = {
            "usuario_id": id,
            "fecha_y_hora_de_inicio": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "fecha_y_hora_finalizacion": None,
            "estado": True,
        }

        self._save(data_to_insert)

    def close_session(self, session_id):
        """
        Cambia el estado de una sesión

        Args:
            session_id (int): el identificador de la sesión
        """

        data_to_update = {
            "fecha_y_hora_finalizacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "estado": False,
        }

        self._update(session_id, data_to_update)

    def find_session_by_active(self):
        """
        Busca una sesión activa
        """
        return self._find_one_by({"estado": True})
