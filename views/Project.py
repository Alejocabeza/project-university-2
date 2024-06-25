import customtkinter as ctk
from tkinter import ttk

from sections.TableModule import TableModule
from sections.HeaderModule import HeaderModule
from controller.Clients.GetAllClientController import GetAllClientController
from controller.Project.CreateProjectController import CreateProjectController
from controller.Project.GetAllProjectController import GetAllProjectController
from controller.Project.RemoveProjectController import RemoveProjectController
from controller.Project.UpdateProjectController import UpdateProjectController
from controller.Address.GetAllAddressController import GetAllAddressController
from controller.Clients.FindClientByIdController import FindClientByIdController
from controller.Employee.GetAllEmployeeController import GetAllEmployeeController
from controller.Project.FindProjectByIdController import FindProjectByIdController
from controller.Address.FindAddressByIdController import FindAddressByIdController
from controller.Employee.FindEmployeeByIdController import FindEmployeeByIdController


class Project(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.find_by_id_address = FindAddressByIdController()
        self.find_by_id_employee = FindEmployeeByIdController()
        self.find_by_id_client = FindClientByIdController()
        self.find_by_id_project = FindProjectByIdController()
        self.create_project_controller = CreateProjectController()
        self.update_project_controller = UpdateProjectController()
        self.remove_project_controller = RemoveProjectController()
        self.get_all_project_controller = GetAllProjectController()
        self.get_all_address_controller = GetAllAddressController()
        self.get_all_employee_controller = GetAllEmployeeController()
        self.get_all_client_controller = GetAllClientController()
        self.options = [
            {"name": "name", "label": "Nombre", "type": "entry"},
            {"name": "start_date", "label": "Fecha de Inicio", "type": "dateentry"},
            {"name": "end_date", "label": "Fecha de Fin", "type": "dateentry"},
            {
                "name": "client",
                "label": "Cliente",
                "type": "combobox",
                "options": self.__get_client_all(),
            },
            {
                "name": "foreman",
                "label": "Maestro de Obra",
                "type": "combobox",
                "options": self.__get_employee_all(),
            },
            {
                "name": "address",
                "label": "Dirección",
                "type": "combobox",
                "options": self.__get_address_all(),
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
        # container
        HeaderModule(
            self.screen,
            "Proyectos",
            self.refresh,
            self.options,
            self.create_project_controller,
        )

    def widget_body(self):
        # container
        data = self.get_all_project_controller.find_all()
        TableModule(
            self.screen,
            {
                "id": "ID",
                "name": "Nombre",
                "description": "Descripción",
                "start_date": "Fecha de Inicio",
                "end_date": "Fecha de Fin",
                "foreman": "Maestro de Obra",
                "address": "Dirección",
                "client": "Cliente",
            },
            data,
            self.find_by_id_project,
            self.options,
            self.update_project_controller,
            self.remove_project_controller,
        )

    def refresh(self):
        self.__clear_widgets(self.screen)
        self.__render_data()

    def close_window_modal(self):
        self.__clear_widgets(self.screen)
        self.__render_data()

    def __clear_widgets(self, widget):
        for w in widget.winfo_children():
            w.destroy()

    def __render_data(self):
        self.widget_header()
        self.widget_body()

    def __get_address_all(self):
        data_to_return = list()
        data = self.get_all_address_controller.find_all()
        if data:
            for address in data:
                data_to_return.append(address.get("name"))
        else:
            data_to_return.append("Sin Dirección")
        return data_to_return

    def __get_employee_all(self):
        data_to_return = list()
        data = self.get_all_employee_controller.find_all()
        if data:
            for employee in data:
                data_to_return.append(employee.get("fullname"))
        else:
            data_to_return.append("Sin Operario")
        return data_to_return

    def __get_client_all(self):
        data_to_return = list()
        data = self.get_all_client_controller.find_all()
        if data:
            for client in data:
                data_to_return.append(client.get("name"))
        else:
            data_to_return.append("Sin cliente")
        return data_to_return

    def __get_address_name(self, id):
        address = self.find_by_id_address.find_by_id(id)
        if address:
            return address.get("name")
        return "Sin Dirección"

    def __get_employee_name(self, id):
        employee = self.find_by_id_employee.find_by_id(id)
        if employee:
            return employee.get("fullname")
        return "Sin Maestro de Obra"

    def __get_client_name(self, id):
        client = self.find_by_id_client.find_by_id(id)
        if client:
            return client.get("name")
        return "Sin Cliente"
