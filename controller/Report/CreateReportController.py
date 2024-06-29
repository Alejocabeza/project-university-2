import os
from datetime import datetime
from services.PDF import create_pdf
from models.ReportModel import ReportModel
from controller.Controller import Controller
from controller.Clients.FindClientByIdController import FindClientByIdController
from controller.Project.FindProjectByIdController import FindProjectByIdController
from controller.Task.FindTaskByProjectController import FindTaskByProjectController


class CreateReportController(Controller):
    def __init__(self):
        super().__init__()
        self.report_repository = ReportModel()
        self.find_project_by_id = FindProjectByIdController()
        self.find_client_by_id = FindClientByIdController()
        self.find_task_by_project = FindTaskByProjectController()

    def create(self, data):
        try:
            data["created_at"] = self._current_time()
            data["path"] = self.generate_pdf(data)
            return self.report_repository.create(data)
        except Exception as ex:
            print(f"Error new report: {ex}")
            return None

    def generate_pdf(self, data):
        project = self.find_project_by_id.find_by_id(data.get("project"))
        client = self.find_client_by_id.find_by_id(project.get("client"))
        current_date = datetime.now()
        start_date = datetime.strptime(f"{project.get("start_date")}", "%Y-%m-%d")
        end_date = datetime.strptime(f"{project.get("end_date")}", "%Y-%m-%d")
        transcurrent_days = end_date - start_date
        remaining_days = end_date - current_date
        tasks = self.find_task_by_project.find_by_project(project.get("id"))
        match data.get("report_type"):
            case 1:
                data_to_insert = {
                    "header_img": "/home/alejocabeza/Workspace/project-university-2/public/img/Grupo Imnova_Logo_2020_2.png",
                    "alt_img": "Grupo Imnova",
                    "current_date": current_date,
                    "number_contract": f"000{project.get('id')}",
                    "start_date_project": project.get("start_date"),
                    "end_date_project": project.get("end_date"),
                    "client_name": client.get("name"),
                    "client_dni": client.get("dni"),
                    "project_description": project.get("description"),
                    "user_name": self._current_user().get("name"),
                    "user_dni": self._current_user().get("dni"),
                    "project_days": project.get("days") or 100,
                    "stop_days": 0,
                    "transcurrent_days": transcurrent_days.days,
                    "additional_days": 0,
                    "remaining_days": remaining_days.days,
                    "tasks": tasks,
                }
                return create_pdf("avance", data_to_insert, data.get("name"))
            case 2:
                data_to_insert = {
                    "header_img": "/home/alejocabeza/Workspace/project-university-2/public/img/Grupo Imnova_Logo_2020_2.png",
                    "alt_img": "Grupo Imnova",
                    "current_date": current_date,
                    "number_contract": f"000{project.get('id')}",
                    "start_date_project": project.get("start_date"),
                    "end_date_project": project.get("end_date"),
                    "client_name": client.get("name"),
                    "client_dni": client.get("dni"),
                    "project_description": project.get("description"),
                    "user_name": self._current_user().get("name"),
                    "user_dni": self._current_user().get("dni"),
                    "project_days": project.get("days") or 100,
                    "stop_days": 0,
                    "transcurrent_days": transcurrent_days.days,
                    "additional_days": 0,
                    "remaining_days": remaining_days.days,
                    "tasks": tasks,
                }
                return create_pdf("finally", data_to_insert, data.get("name"))
