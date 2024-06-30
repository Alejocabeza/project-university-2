from models.BaseModel import BaseModel


class EmployeeModel(BaseModel):
    def __init__(self):
        super().__init__("employee")

    def create_employee(self, data):
        return self._save(data)

    def update_employee(self, id, data):
        return self._update(id, data)

    def remove_employee(self, id):
        return self._remove(id)

    def employee_all(self):
        return self._find_all()

    def find_employee_by_id(self, id):
        return self._find_one_by({"id": id})

    def find_employee_by_fullname(self, fullname):
        return self._find_one_by({"fullname": fullname})

    def find_by_user(self, user_id):
        """
        Buscar un registro por el usuario

        Args:
            user_id (int): El identificador del usuario
        """
        return self._find_by({"created_by": user_id})
