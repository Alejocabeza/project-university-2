from controller.Controller import Controller
from models.ProjectModel import ProjectModel


class GetAllProjectController(Controller):
    def __init__(self):
        super().__init__()
        self.project_repository = ProjectModel()

    def find_all(self):
        try:
            return self.project_repository.find_all()
        except Exception as ex:
            print(f"Error finder all GetAllProject: {ex}")
            return None
