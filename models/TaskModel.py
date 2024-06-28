
from models.BaseModel import BaseModel

class TaskModel(BaseModel):
    def __init__(self):
        super().__init__('task')

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

    def find_by_project(self, id):
        return self._find_by({"project": id})