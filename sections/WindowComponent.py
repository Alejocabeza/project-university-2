import re
import customtkinter as ctk

from lib.util_window import window_center
from controller.Address.FindAddressByMainAddressController import (
    FindAddressByMainAddressController,
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
        self.find_address_by_main_address_controller = (
            FindAddressByMainAddressController()
        )
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
        self.screen = ctk.CTkScrollableFrame(
            self, fg_color="transparent", corner_radius=0
        )
        self.screen.pack(expand=ctk.YES, fill=ctk.BOTH)

        self.container = ctk.CTkFrame(
            self.screen, fg_color="transparent", corner_radius=5
        )
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
                text_color="white",
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
                        placeholder_text=placeholder,
                        show=show,
                    )
                    self.entry.pack(expand=ctk.NO, fill=ctk.X)
                    self.inputs[field["name"]] = self.entry
                case "combobox":
                    self.combobox = ctk.CTkComboBox(
                        self.input_container, values=field["options"]
                    )
                    self.combobox.pack(expand=ctk.NO, fill=ctk.X)
                    self.combobox.set(self.get_combobox_value(field['name']))
                    self.inputs[field["name"]] = self.combobox

    def create_button_submit(self):
        if not self.show_errors:
            self.btn_submit = ctk.CTkButton(
                self.container,
                text="Guardar",
                command=self.on_submit,
            )
            self.btn_submit.pack(fill=ctk.X, pady=20)

            if self.type_action == "update":
                self.btn_remove = ctk.CTkButton(
                    self.container,
                    text="Eliminar",
                    command=self.on_remove,
                    fg_color="red",
                )
                self.btn_remove.pack(fill=ctk.X, pady=5)
        else:
            print(self.errors)
            self.__clear_widgets(self.container)
            self.__render_data()

    def on_submit(self):
        try:
            res = False
            print(self.__get_input_data())
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
                if name == "role":
                    rol = widget.get()
                    if rol == "Administrador":
                        data[name.lower()] = "admin"
                    elif rol == "Usuario":
                        data[name.lower()] = "user"
                if name == "address":
                    print(widget.get())

        if not new_errors:
            return data

    def __set_placeholder(self, name):
        if self.type_action == "update":
            return self.values.get(name)
        else:
            return ""

    def get_combobox_value(self, name):
        match name:
            case "role":
                if self.type_action == "update":
                    match self.values.get("role"):
                        case "user":
                            return "Usuario"
                        case "admin":
                            return "Administrador"
                else:
                    return ""
            case "address":
                if self.type_action == "update":
                    print(self.values.get('role'))
                else:
                    return ""
            case _:
                return ""