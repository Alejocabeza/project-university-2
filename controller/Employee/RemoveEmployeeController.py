from controller.Controller import Controller
from models.EmployeeModel import EmployeeModel


class RemoveEmployeeController(Controller):
    def __init__(self):
        super().__init__()
        self.employee_repository = EmployeeModel()

    def remove(self, id):
        try:
            return self.employee_repository.remove_employee(id)
        except Exception as e:
            print(f"Error al eliminar un empleado: {e}")
            return None
