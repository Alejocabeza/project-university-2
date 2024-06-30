from models.BaseModel import BaseModel


class ProjectModel(BaseModel):
    def __init__(self):
        super().__init__("project")

    def create(self, data):
        return self._save(data)

    def update(self, id, data):
        return self._update(id, data)

    def remove(self, id):
        return self._remove(id)

    def find_all(self):
        return self._find_all()

    def find_by_id(self, id):
        return self._find_one_by({"id": id})

    def find_by_name(self, name):
        return self._find_one_by({"name": name})

    def find_by_user(self, user_id):
        """
        Buscar un registro por el usuario

        Args:
            user_id (int): El identificador del usuario
        """
        return self._find_by({"created_by": user_id})
