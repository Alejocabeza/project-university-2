from controller.Controller import Controller
from models.ReportModel import ReportModel


class GetAllReportController(Controller):
    def __init__(self):
        super().__init__()
        self.report_repository = ReportModel()

    def find_all(self):
        try:
            if self._current_user().get("role") == "admin":
                return self.report_repository.find_all()
            else:
                return self.report_repository.find_by_user(
                    self._current_user().get("id")
                )
        except Exception as ex:
            print(f"Error finder all GetAllReport: {ex}")
            return None
