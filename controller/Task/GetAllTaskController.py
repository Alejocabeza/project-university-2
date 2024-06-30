from controller.Controller import Controller
from models.TaskModel import TaskModel


class GetAllTaskController(Controller):
    def __init__(self):
        super().__init__()
        self.task_repository = TaskModel()

    def find_all(self):
        try:
            if self._current_user().get("role") == "admin":
                return self.task_repository.find_all()
            else:
                return self.task_repository.find_by_user(self._current_user().get("id"))
        except Exception as ex:
            print(f"Error finder all GetAllTask: {ex}")
            return None
