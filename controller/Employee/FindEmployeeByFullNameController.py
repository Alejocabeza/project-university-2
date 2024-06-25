from controller.Controller import Controller
from models.EmployeeModel import EmployeeModel


class FindEmployeeByFullNameController(Controller):
    def __init__(self):
        super().__init__()
        self.employee_repository = EmployeeModel()

    def find_by_fullname(self, fullname):
        try:
            return self.employee_repository.find_employee_by_fullname(fullname)
        except Exception as ex:
            print(f"cannot find employee by fullname: {fullname}")
            return None
