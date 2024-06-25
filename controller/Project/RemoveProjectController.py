from controller.Controller import Controller
from models.ProjectModel import ProjectModel


class RemoveProjectController(Controller):
    def __init__(self):
        super().__init__()
        self.project_repository = ProjectModel()

    def remove(self, id, data):
        try:
            return self.project_repository.update(id, data)
        except Exception as ex:
            print(f"Error update RemoveProject: {ex}")
            return None
