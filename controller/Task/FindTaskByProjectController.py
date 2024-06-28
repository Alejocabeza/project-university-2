
from controller.Controller import Controller
from models.TaskModel import TaskModel

class FindTaskByProjectController(Controller):
    def __init__(self):
        super().__init__()
        self.task_repository = TaskModel()
    
    def find_by_project(self, project_id):
        try:
            return self.task_repository.find_by_project(project_id)
        except Exception as ex:
            print("cannot find task by project")
            return None
