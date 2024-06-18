from controller.Controller import Controller
from models.EmployeeModel import EmployeeModel


class CreateEmployeeController(Controller):
    def __init__(self):
        super().__init__()
        self.employee_repository = EmployeeModel()

    def create(self, data):
        try:
            data['created_by'] = self._current_user().get('id')
            return self.employee_repository.create_employee(data)
        except Exception as e:
            print(f"Error al crear un empleado: {e}")
            return None
