
from controller.Controller import Controller
from models.ReportModel import ReportModel

class GetAllReportController(Controller):
    def __init__(self):
        super().__init__()
        self.report_repository = ReportModel()

    def find_all(self):
        try:
            return self.report_repository.find_all()
        except Exception as ex:
            print(f"Error finder all GetAllReport: {ex}")
            return None
