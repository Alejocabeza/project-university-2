
from controller.Controller import Controller
from models.TaskModel import TaskModel

class FindByIdTaskController(Controller):
    def __init__(self):
        super().__init__()
        self.task_repository = TaskModel()

    def find_by_id(self, id):
        try:
            return self.task_repository.find_by_id(id)
        except Exception as ex:
            print(f"Cannot find FindByIdTask by id: {ex}")
            return None
