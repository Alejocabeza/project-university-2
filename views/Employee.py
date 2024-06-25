import customtkinter as ctk

from sections.TableModule import TableModule
from sections.HeaderModule import HeaderModule
from controller.Employee.CreateEmployeeController import CreateEmployeeController
from controller.Employee.GetAllEmployeeController import GetAllEmployeeController
from controller.Employee.RemoveEmployeeController import RemoveEmployeeController
from controller.Employee.UpdateEmployeeController import UpdateEmployeeController
from controller.Employee.FindEmployeeByIdController import FindEmployeeByIdController


class Employee(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_employee_controller = CreateEmployeeController()
        self.update_employee_controller = UpdateEmployeeController()
        self.remove_employee_controller = RemoveEmployeeController()
        self.get_all_employee_controller = GetAllEmployeeController()
        self.find_employee_by_id_controller = FindEmployeeByIdController()
        self.options = [
            {"name": "firstname", "label": "Nombre", "type": "entry"},
            {"name": "lastname", "label": "Apellido", "type": "entry"},
            {"name": "dni", "label": "Cédula/RIF", "type": "entry"},
            {"name": "email", "label": "Email", "type": "entry"},
            {"name": "phone", "label": "Teléfono", "type": "entry"},
        ]
        self.widgets()
        self.widget_header()
        self.widget_body()

    def widgets(self):
        self.screen = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.screen.pack(expand=ctk.YES, fill=ctk.BOTH)

    def widget_header(self):
        HeaderModule(
            self.screen,
            "Operarios",
            self.refresh,
            self.options,
            self.create_employee_controller,
        )

    def widget_body(self):
        data = self.get_all_employee_controller.find_all()
        TableModule(
            self.screen,
            {
                "id": "ID",
                "firstname": "Nombre",
                "lastname": "Apellido",
                "dni": "DNI/RIF",
                "email": "Email",
                "phone": "Telefono",
            },
            data,
            self.find_employee_by_id_controller,
            self.options,
            self.update_employee_controller,
            self.remove_employee_controller,
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
