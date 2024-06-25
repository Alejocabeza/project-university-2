from controller.Controller import Controller
from models.EmployeeModel import EmployeeModel


class FindEmployeeByIdController(Controller):
    def __init__(self):
        super().__init__()
        self.employee_repository = EmployeeModel()

    def find_by_id(self, id):
        try:
            return self.employee_repository.find_employee_by_id(id)
        except Exception as e:
            print(f"Error finding employee: {e}")
            return None
