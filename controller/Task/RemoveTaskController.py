
from controller.Controller import Controller
from models.TaskModel import TaskModel

class RemoveTaskController(Controller):
    def __init__(self):
        super().__init__()
        self.task_repository = TaskModel()

    def remove(self, id):
        try:
            return self.task_repository.update(id, {'deleted_at': self._current_time()})
        except Exception as ex:
            print(f"Error remove RemoveTask: {ex}")
            return None
