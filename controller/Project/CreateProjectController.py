from controller.Controller import Controller
from models.ProjectModel import ProjectModel


class CreateProjectController(Controller):
    def __init__(self):
        super().__init__()
        self.project_repository = ProjectModel()

    def create(self, data):
        try:
            data["created_at"] = self._current_time()
            return self.project_repository.create(data)
        except Exception as ex:
            print(f"Error new project: {ex}")
            return None
