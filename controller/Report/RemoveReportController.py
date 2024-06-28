
from controller.Controller import Controller
from models.ReportModel import ReportModel

class RemoveReportController(Controller):
    def __init__(self):
        super().__init__()
        self.report_repository = ReportModel()

    def remove(self, id):
        try:
            return self.report_repository.update(id, {'deleted_at': self._current_time()})
        except Exception as ex:
            print(f"Error remove RemoveReport: {ex}")
            return None
