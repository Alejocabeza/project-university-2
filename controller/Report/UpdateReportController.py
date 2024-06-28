
from controller.Controller import Controller
from models.ReportModel import ReportModel

class UpdateReportController(Controller):
    def __init__(self):
        super().__init__()
        self.report_repository = ReportModel()

    def update(self, id, data):
        try:
            data['updated_at'] = self._current_time()
            return self.report_repository.update(id, data)
        except Exception as ex:
            print(f"Error update UpdateReport: {ex}")
            return None
