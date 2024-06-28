
from models.BaseModel import BaseModel

class ReportModel(BaseModel):
    def __init__(self):
        super().__init__('report')

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
