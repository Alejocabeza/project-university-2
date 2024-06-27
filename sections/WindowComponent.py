import re
from tkinter import ttk
import customtkinter as ctk
from tkcalendar import DateEntry

from lib.util_window import window_center
from controller.Clients.FindClientByIdController import FindClientByIdController
from controller.Address.FindAddressByIdController import FindAddressByIdController
from controller.Project.FindProjectByIdController import FindProjectByIdController
from controller.Clients.FindClientByNameController import FindClientByNameController
from controller.Employee.FindEmployeeByIdController import FindEmployeeByIdController
from controller.Address.FindAddressByNameController import FindAddressByNameController
from controller.Project.FindProjectByNameController import FindProjectByNameController
from controller.ClientOffice.FindClientOfficeByIdController import (
    FindClientOfficeByIdController,
)
from controller.Employee.FindEmployeeByFullNameController import (
    FindEmployeeByFullNameController,
)
from controller.ClientOffice.FindClientOfficeByNameController import (
    FindClientOfficeByNameController,
)
from config import (
    TWO_COLOR,
    ONE_COLOR,
    THREE_COLOR,
    THREE_COLOR_HOVER,
    COLOR_RED_PRIMARY,
    COLOR_RED_SECONDARY,
)


class WindowComponent(ctk.CTkToplevel):
    def __init__(
        self,
        field_options,
        controller,
        window_name,
        type,
        values,
        ctrl_remove,
        width=450,
        height=600,
    ):
        super().__init__()
        self.find_client_by_name = FindClientByNameController()
        self.find_address_by_name = FindAddressByNameController()
        self.find_employee_by_fullname = FindEmployeeByFullNameController()
        self.find_client_office_by_name = FindClientOfficeByNameController()
        self.find_client_by_id = FindClientByIdController()
        self.find_address_by_id = FindAddressByIdController()
        self.find_employee_by_id = FindEmployeeByIdController()
        self.find_client_office_by_id = FindClientOfficeByIdController()
        self.find_project_by_id = FindProjectByIdController()
        self.find_project_by_name = FindProjectByNameController()
        self.width = width
        self.height = height
        self.show_errors = False
        self.type_action = type
        self.field_options = field_options
        self.controller = controller
        self.errors = {}
        self.inputs = {}
        self.window_name = window_name
        self.ctrl_remove = ctrl_remove
        self.values = values
        self.window_config()
        self.main_widget()
        self.create_input_field()
        self.create_button_submit()

    def window_config(self):
        self.title(self.window_name)
        self.resizable(False, False)
        window_center(self, self.width, self.height)

    def main_widget(self):
        self.screen = ctk.CTkScrollableFrame(self, fg_color=TWO_COLOR, corner_radius=0)
        self.screen.pack(expand=ctk.YES, fill=ctk.BOTH)

        self.container = ctk.CTkFrame(self.screen, fg_color=TWO_COLOR, corner_radius=5)
        self.container.pack(expand=ctk.YES, fill=ctk.BOTH, pady=40, padx=20)

        self.label = ctk.CTkLabel(
            self.container,
            text_color="white",
            text=self.window_name,
            font=("Roboto", 30),
            anchor="w",
        )
        self.label.pack(side=ctk.TOP, fill=ctk.X, expand=ctk.NO)

    def create_input_field(self):
        for field in self.field_options:
            self.input_container = ctk.CTkFrame(self.container, fg_color="transparent")
            self.input_container.pack(expand=ctk.NO, fill=ctk.BOTH, pady=5)
            self.input_label = ctk.CTkLabel(
                self.input_container,
                text=field["label"],
                text_color=ONE_COLOR,
                anchor="w",
            )
            self.input_label.pack(side=ctk.TOP, fill=ctk.X, expand=ctk.NO)
            placeholder = self.__set_placeholder(field["name"])
            match field["type"]:
                case "entry":
                    show = ""
                    if field["name"] == "password":
                        show = "*"
                    self.entry = ctk.CTkEntry(
                        self.input_container,
                        fg_color="transparent",
                        bg_color="transparent",
                        border_color=ONE_COLOR,
                        placeholder_text=placeholder,
                        show=show,
                    )
                    self.entry.pack(expand=ctk.NO, fill=ctk.X)
                    self.inputs[field["name"]] = self.entry
                case "textbox":
                    self.textarea = ctk.CTkTextbox(
                        self.input_container,
                        fg_color="transparent",
                        bg_color="transparent",
                        height=150,
                        border_color=ONE_COLOR,
                        border_width=2,
                    )
                    self.textarea.pack(expand=ctk.NO, fill=ctk.X)
                    if self.type_action == "update":
                        self.textarea.insert(ctk.INSERT, self.values.get(field["name"]))
                    self.inputs[field["name"]] = self.textarea
                case "dateentry":
                    self.calender = DateEntry(
                        self.input_container,
                        background=TWO_COLOR,
                        foreground=ONE_COLOR,
                        date_pattern="yyyy-mm-dd",
                    )
                    self.calender.pack(expand=ctk.NO, fill=ctk.X)
                    if self.type_action == "update":
                        self.calender.set_date(self.values.get(field["name"]))
                    self.inputs[field["name"]] = self.calender
                case "combobox":
                    self.combobox = ctk.CTkComboBox(
                        self.input_container,
                        values=field["options"],
                        fg_color=TWO_COLOR,
                        border_color=ONE_COLOR,
                    )
                    self.combobox.pack(expand=ctk.NO, fill=ctk.X)
                    self.combobox.set(self.get_combobox_value(field["name"]))
                    self.inputs[field["name"]] = self.combobox

    def create_button_submit(self):
        if not self.show_errors:
            self.btn_submit = ctk.CTkButton(
                self.container,
                text="Guardar",
                command=self.on_submit,
                fg_color=THREE_COLOR,
                hover_color=THREE_COLOR_HOVER,
            )
            self.btn_submit.pack(fill=ctk.X, pady=20)

            if self.type_action == "update":
                self.btn_remove = ctk.CTkButton(
                    self.container,
                    text="Eliminar",
                    command=self.on_remove,
                    fg_color=COLOR_RED_PRIMARY,
                    hover_color=COLOR_RED_SECONDARY,
                )
                self.btn_remove.pack(fill=ctk.X, pady=5)
        else:
            print(self.errors)
            self.__clear_widgets(self.container)
            self.__render_data()

    def on_submit(self):
        try:
            res = False
            if self.type_action == "update":
                res = self.controller.update(
                    self.values.get("id"), self.__get_input_data()
                )
            else:
                res = self.controller.create(self.__get_input_data())

            if res:
                self.destroy()
        except Exception as ex:
            print(f"Error al ejecutar la petición: {ex}")
            return None

    def on_remove(self):
        try:
            self.ctrl_remove.remove(self.values.get("id"))
            self.destroy()
        except Exception as ex:
            print(f"Error al remover el usuario: {ex}")
            return None

    def __clear_widgets(self, widget):
        for w in widget.winfo_children():
            w.destroy()

    def __render_data(self):
        self.show_errors = False
        self.create_input_field()
        self.create_button_submit()

    def __get_input_data(self):
        data = {}
        self.errors.clear()
        self.show_errors = False
        new_errors = False

        for name, widget in self.inputs.items():
            if isinstance(widget, ctk.CTkEntry):
                value = widget.get()
                if not value and self.type_action != "update":
                    self.show_errors = True
                    new_errors = True
                    widget.configure(border_color="red")
                    self.errors[name] = "Este campo es requerido"
                else:
                    if name == "Email":
                        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
                        if not re.match(email_pattern, value):
                            self.show_errors = True
                            new_errors = True
                            widget.configure(border_color="red")
                            self.errors[name] = "Debe tener un formato válido"
                        else:
                            widget.configure(border_color="green")
                            data[name.lower()] = value
                    elif name == "Contraseña":
                        password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&.])[A-Za-z\d@$!%*?&.]{8,}$"
                        if not re.match(password_pattern, value):
                            self.show_errors = True
                            new_errors = True
                            widget.configure(border_color="red")
                            self.errors[name] = "Debe ser una contraseña fuerte"
                        else:
                            widget.configure(border_color="green")
                            data[name] = value
                    else:
                        widget.configure(border_color="green")
                        if value:
                            data[name.lower()] = value
            elif isinstance(widget, ctk.CTkComboBox):
                match name:
                    case "role":
                        rol = widget.get()
                        if rol == "Administrador":
                            data[name.lower()] = "admin"
                        elif rol == "Usuario":
                            data[name.lower()] = "user"
                    case "address":
                        value = widget.get()
                        if value and value != "Sin Dirección":
                            address = self.find_address_by_name.find_by_name(value)
                            data[name.lower()] = address.get("id")
                    case "foreman":
                        value = widget.get()
                        if value and value != "Sin Operador":
                            foreman = self.find_employee_by_fullname.find_by_fullname(
                                value
                            )
                            data[name.lower()] = foreman.get("id")
                    case "employee":
                        value = widget.get()
                        if value and value != "Sin Operario":
                            employee = self.find_employee_by_fullname.find_by_fullname(
                                value
                            )
                            data[name.lower()] = employee.get("id")
                    case "client_office":
                        value = widget.get()
                        if value and value != "Sin Sucursal":
                            office = self.find_client_office_by_name.find_by_name(
                                widget.get()
                            )
                            data[name.lower()] = office.get("id")
                    case "client":
                        value = widget.get()
                        if value and value != "Sin Cliente":
                            client = self.find_client_by_name.find_by_name(value)
                            data[name.lower()] = client.get("id")
                    case "project":
                        value = widget.get()
                        if value and value != "Sin Proyectos":
                            project = self.find_project_by_name.find_by_name(value)
                            data[name.lower()] = project.get("id")
                    case "status":
                        value = widget.get()
                        if value == "Pendiente":
                            data[name.lower()] = 1
                        elif value == "En Proceso":
                            data[name.lower()] = 2
                        else:
                            data[name.lower()] = 3
                    case "type":
                        type_option = widget.get()
                        if type_option == "Persona Natural":
                            data[name.lower()] = "person"
                        elif type_option == "Persona Jurídica":
                            data[name.lower()] = "company"
                        else:
                            data[name.lower()] = "government"
                    case _:
                        data[name.lower()] = widget.get()
            elif isinstance(widget, ctk.CTkTextbox):
                text = widget.get("0.0", "end")
                if text and text != "":
                    data[name.lower()] = text
            elif isinstance(widget, DateEntry):
                date = widget.get_date()
                if date:
                    data[name.lower()] = date.strftime("%Y-%m-%d")

        if not new_errors:
            return data

    def __set_placeholder(self, name):
        if self.type_action == "update":
            return self.values.get(name)
        else:
            return ""

    def get_combobox_value(self, name):
        if self.type_action == "update":
            match name:
                case "type":
                    if self.values.get(name) and self.values.get(name) != "Sin Tipo":
                        match self.values.get(name):
                            case "person":
                                return "Persona Natural"
                            case "company":
                                return "Persona Jurídica"
                            case "government":
                                return "Gubernamental"
                    return "Sin Tipo"
                case "address":
                    if (
                        self.values.get(name)
                        and self.values.get(name) != "Sin Dirección"
                    ):
                        return self.find_address_by_id.find_by_id(
                            self.values.get(name)
                        ).get("name")
                    return "Sin Dirección"
                case "foreman":
                    if (
                        self.values.get(name)
                        and self.values.get(name) != "Sin Operador"
                    ):
                        return self.find_employee_by_id.find_by_id(
                            self.values.get(name)
                        ).get("fullname")
                    return "Sin Maestro de Obra"
                case 'employee':
                    if (
                        self.values.get(name)
                        and self.values.get(name) != "Sin Operador"
                    ):
                        return self.find_employee_by_id.find_by_id(
                            self.values.get(name)
                        ).get("fullname")
                    return "Sin Operador"
                case "client_office":
                    if (
                        self.values.get(name)
                        and self.values.get(name) != "Sin Sucursal"
                    ):
                        return self.find_client_office_by_id.find_by_id(
                            self.values.get(name)
                        ).get("name")
                    return "Sin Sucursal"
                case "client":
                    if self.values.get(name) and self.values.get(name) != "Sin Cliente":
                        return self.find_client_by_id.find_by_id(
                            self.values.get(name)
                        ).get("name")
                    return "Sin Cliente"
                case "project":
                    if (
                        self.values.get(name)
                        and self.values.get(name) != "Sin Proyecto"
                    ):
                        return self.find_project_by_id.find_by_id(
                            self.values.get(name)
                        ).get("name")
                    return "Sin Proyecto"
                case 'status':
                    if self.values.get(name) == 1:
                        return "Pendiente"
                    elif self.values.get(name) == 2:
                        return "En Proceso"
                    else:
                        return "Finalizado"
                case _:
                    return self.values.get(name)
        return ""
