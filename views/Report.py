import os
import platform
import customtkinter as ctk

from sections.TableModule import TableModule
from sections.HeaderModule import HeaderModule
from controller.Report.CreateReportController import CreateReportController
from controller.Report.GetAllReportController import GetAllReportController
from controller.Report.RemoveReportController import RemoveReportController
from controller.Report.UpdateReportController import UpdateReportController
from controller.Project.GetAllProjectController import GetAllProjectController
from controller.Report.FindByIdReportController import FindByIdReportController


class Report(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_report_controller = CreateReportController()
        self.update_report_controller = UpdateReportController()
        self.remove_report_controller = RemoveReportController()
        self.get_all_report_controller = GetAllReportController()
        self.get_all_project_controller = GetAllProjectController()
        self.find_report_by_id_controller = FindByIdReportController()
        self.options = [
            {"name": "name", "label": "Titulo", "type": "entry"},
            {
                "name": "project",
                "label": "Proyecto",
                "type": "combobox",
                "options": self.__get_project_all(),
            },
            {
                "name": "report_type",
                "label": "Tipo de Reporte",
                "type": "combobox",
                "options": [
                    "Informe de Avance de Obra",
                    "Informe de Entrega de Obra",
                ],
            },
        ]
        self.widgets()
        self.widget_header()
        self.widget_body()
        self.window_modal = None

    def widgets(self):
        self.screen = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.screen.pack(expand=ctk.YES, fill=ctk.BOTH)

    def widget_header(self):
        # container
        HeaderModule(
            self.screen,
            "Reportes",
            self.refresh,
            self.options,
            self.create_report_controller,
        )

    def widget_body(self):
        # container
        data = self.get_all_report_controller.find_all()
        TableModule(
            self.screen,
            {
                "id": "ID",
                "name": "Titulo",
                "project": "Proyecto",
                "report_type": "Tipo de Reporte",
            },
            data,
            self.find_report_by_id_controller,
            self.options,
            self.update_report_controller,
            self.remove_report_controller,
            type="report",
        )

    def refresh(self):
        self.__clear_widgets(self.screen)
        self.__render_data()

    def __clear_widgets(self, widget):
        for w in widget.winfo_children():
            w.destroy()

    def __get_project_all(self):
        data_to_return = []
        data = self.get_all_project_controller.find_all()
        if data:
            for project in data:
                data_to_return.append(project.get("name"))
        else:
            data_to_return.append("Sin Proyectos")
        return data_to_return

    def __render_data(self):
        self.widget_header()
        self.widget_body()
