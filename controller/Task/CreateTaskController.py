from controller.Controller import Controller
from models.TaskModel import TaskModel


class CreateTaskController(Controller):
    def __init__(self):
        super().__init__()
        self.task_repository = TaskModel()

    def create(self, data):
        try:
            data["created_at"] = self._current_time()
            print(data)
            return self.task_repository.create(data)
        except Exception as ex:
            print(f"Error new task: {ex}")
            return None
