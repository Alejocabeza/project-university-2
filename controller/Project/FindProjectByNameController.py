
from controller.Controller import Controller
from models.ProjectModel import ProjectModel

class FindProjectByNameController(Controller):
    def __init__(self):
        super().__init__()
        self.project_repository = ProjectModel()

    def find_by_name(self, name):
        try:
            return self.project_repository.find_by_name(name)
        except Exception as ex:
            print(f"Error al buscar el proyecto: {ex}")
            return None
