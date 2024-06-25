
from controller.Controller import Controller
from models.ProjectModel import ProjectModel

class UpdateProjectController(Controller):
    def __init__(self):
        super().__init__()
        self.project_repository = ProjectModel()

    def create(self, id, data):
        try:
            data['updated_at'] = self._current_time()
            self.project_repository.update(id, data)
        except Exception as ex:
            print(f"Error update UpdateProject: {ex}")
            return None
