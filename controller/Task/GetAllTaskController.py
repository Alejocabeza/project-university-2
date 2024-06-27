
from controller.Controller import Controller
from models.TaskModel import TaskModel

class GetAllTaskController(Controller):
    def __init__(self):
        super().__init__()
        self.task_repository = TaskModel()

    def find_all(self):
        try:
            return self.task_repository.find_all()
        except Exception as ex:
            print(f"Error finder all GetAllTask: {ex}")
            return None
