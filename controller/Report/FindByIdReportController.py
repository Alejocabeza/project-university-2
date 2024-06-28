
from controller.Controller import Controller
from models.ReportModel import ReportModel

class FindByIdReportController(Controller):
    def __init__(self):
        super().__init__()
        self.report_repository = ReportModel()

    def find_by_id(self, id):
        try:
            return self.report_repository.find_by_id(id)
        except Exception as ex:
            print(f"Cannot find FindByIdReport by id: {ex}")
            return None
