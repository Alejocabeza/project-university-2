from controller.Controller import Controller
from models.EmployeeModel import EmployeeModel


class GetAllEmployeeController(Controller):
    def __init__(self):
        super().__init__()
        self.employee_repository = EmployeeModel()

    def find_all(self):
        try:
            if self._current_user().get("role") == "admin":
                return self.employee_repository.employee_all()
            else:
                return self.employee_repository.find_by_user(
                    self._current_user().get("id")
                )
        except Exception as e:
            print(f"Error al optener todos los empleados: {e}")
            return None
