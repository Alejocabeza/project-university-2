from controller.Controller import Controller
from models.ProjectModel import ProjectModel


class FindProjectByIdController(Controller):
    def __init__(self):
        super().__init__()
        self.project_repository = ProjectModel()

    def find_by_id(self, id):
        try:
            return self.project_repository.find_by_id(id)
        except Exception as e:
            print(f"Cannot find project by id: {e}")
            return None
