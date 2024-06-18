from controller.Controller import Controller
from models.EmployeeModel import EmployeeModel


class UpdateEmployeeController(Controller):
    def __init__(self):
        super().__init__()
        self.employee_repository = EmployeeModel()

    def update(self, id, data):
        try:
            data['updated_by'] = self._current_user().get('id')
            return self.employee_repository.update_employee(id, data)
        except Exception as e:
            print(f"Error al actualizar un empleado: {e}")
            return None
