
from controller.Controller import Controller
from models.TaskModel import TaskModel

class UpdateTaskController(Controller):
    def __init__(self):
        super().__init__()
        self.task_repository = TaskModel()

    def update(self, id, data):
        try:
            data['updated_at'] = self._current_time()
            return self.task_repository.update(id, data)
        except Exception as ex:
            print(f"Error update UpdateTask: {ex}")
            return None
