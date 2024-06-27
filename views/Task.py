import customtkinter as ctk

from sections.TableModule import TableModule
from sections.HeaderModule import HeaderModule
from controller.Task.CreateTaskController import CreateTaskController
from controller.Task.GetAllTaskController import GetAllTaskController
from controller.Task.RemoveTaskController import RemoveTaskController
from controller.Task.UpdateTaskController import UpdateTaskController
from controller.Task.FindByIdTaskController import FindByIdTaskController
from controller.Project.GetAllProjectController import GetAllProjectController
from controller.Employee.GetAllEmployeeController import GetAllEmployeeController


class Task(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_task_controller = CreateTaskController()
        self.update_task_controller = UpdateTaskController()
        self.remove_task_controller = RemoveTaskController()
        self.get_all_task_controller = GetAllTaskController()
        self.find_task_by_id_controller = FindByIdTaskController()
        self.get_all_project_controller = GetAllProjectController()
        self.get_all_employee_controller = GetAllEmployeeController()
        self.options = [
            {"name": "name", "label": "Nombre", "type": "entry"},
            {"name": "start_date", "label": "Fecha de Inicio", "type": "dateentry"},
            {"name": "end_date", "label": "Fecha de Fin", "type": "dateentry"},
            {
                "name": "project",
                "label": "Proyecto",
                "type": "combobox",
                "options": self.__get_project_all(),
            },
            {
                "name": "employee",
                "label": "Operario",
                "type": "combobox",
                "options": self.__get_employee_all(),
            },
            {
                "name": "status",
                "label": "Estado",
                "type": "combobox",
                "options": ["Pendiente", "En Proceso", "Finalizada"],
            },
            {"name": "description", "label": "Descripción", "type": "textbox"},
        ]
        self.widgets()
        self.widget_header()
        self.widget_body()
        self.window_modal = None

    def widgets(self):
        self.screen = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.screen.pack(expand=ctk.YES, fill=ctk.BOTH)

    def widget_header(self):
        HeaderModule(
            self.screen,
            "Tarea",
            self.refresh,
            self.options,
            self.create_task_controller,
            height=680,
        )

    def widget_body(self):
        data = self.get_all_task_controller.find_all()
        TableModule(
            self.screen,
            {
                "id": "ID",
                "name": "Nombre",
                "description": "Descripción",
                "start_date": "Fecha de Inicio",
                "end_date": "Fecha de Fin",
                "project": "Proyecto",
                "employee": "Operario",
                "status": "Estado",
            },
            data,
            self.find_task_by_id_controller,
            self.options,
            self.update_task_controller,
            self.remove_task_controller,
            height=680,
        )

    def refresh(self):
        self.__clear_widgets(self.screen)
        self.__render_data()

    def __clear_widgets(self, widget):
        for w in widget.winfo_children():
            w.destroy()

    def __render_data(self):
        self.widget_header()
        self.widget_body()

    def __get_project_all(self):
        data_to_return = []
        data = self.get_all_project_controller.find_all()
        if data:
            for project in data:
                data_to_return.append(project.get("name"))
        else:
            data_to_return.append("Sin Proyectos")
        return data_to_return

    def __get_employee_all(self):
        data_to_return = []
        data = self.get_all_employee_controller.find_all()
        if data:
            for employee in data:
                data_to_return.append(employee.get("name"))
        else:
            data_to_return.append("Sin Operario")
        return data_to_return
