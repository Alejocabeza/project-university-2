import re
import customtkinter as ctk
from controller.Auth.AuthRegisterController import AuthRegisterController


class Register(ctk.CTkFrame):
    """
    Muestra el frame de Crear una Cuenta
    """

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.show_errors = False
        self.create_widgets()
        self.auth_register_controller = AuthRegisterController()
        self.error_labels = []

    def create_widgets(self):
        # screen
        self.screen = ctk.CTkFrame(self)
        self.screen.pack(fill=ctk.BOTH, expand=ctk.YES)

        self.container = ctk.CTkScrollableFrame(
            self.screen,
        )
        self.container.pack(fill=ctk.BOTH, expand=ctk.YES)

        self.title = ctk.CTkLabel(
            self.container, text="Crear una Cuenta", font=("Arial", 30)
        )
        self.title.pack(pady=20)

        # input Name
        self.label = ctk.CTkLabel(
            self.container, text="Nombre", font=("Arial", 15), width=500, anchor="w"
        )
        self.label.pack()
        self.input_name = ctk.CTkEntry(
            self.container, placeholder_text="Escribe aquí tu nombre...", width=500
        )
        self.input_name.focus()
        self.input_name.pack(pady=5)
        # input Email
        self.label = ctk.CTkLabel(
            self.container, text="Email", font=("Arial", 15), width=500, anchor="w"
        )
        self.label.pack()
        self.input_email = ctk.CTkEntry(
            self.container, placeholder_text="Escribe aquí tu email...", width=500
        )
        self.input_email.pack(pady=5)

        # input Password
        self.label = ctk.CTkLabel(
            self.container, text="Contraseña", font=("Arial", 15), width=500, anchor="w"
        )
        self.label.pack()
        self.input_password = ctk.CTkEntry(
            self.container,
            placeholder_text="Escribe tu contraseña...",
            width=500,
            show="*",
        )
        self.input_password.pack(pady=5)

        # input confirmed Password
        self.label = ctk.CTkLabel(
            self.container,
            text="Confirmar Contraseña",
            font=("Arial", 15),
            width=500,
            anchor="w",
        )
        self.label.pack()
        self.input_confirmed_password = ctk.CTkEntry(
            self.container,
            placeholder_text="Confirma tu contraseña...",
            width=500,
            show="*",
        )
        self.input_confirmed_password.pack(pady=5)

        # Button Box
        self.container_buttons = ctk.CTkFrame(
            self.container, bg_color="transparent", fg_color="transparent"
        )
        self.container_buttons.pack(pady=10)
        # Button Register
        self.btn_login = ctk.CTkButton(
            self.container_buttons,
            bg_color="transparent",
            fg_color="transparent",
            text="Ya tienes una cuenta?",
            command=lambda: self.controller.show_frame("Login"),
        )
        self.btn_login.pack(side="left")

        # Button Submit
        self.btn_submit = ctk.CTkButton(
            self.container_buttons,
            text="Craer Cuenta",
            command=lambda: self.__handle_submit(),
        )
        self.btn_submit.pack(side="right", padx=8)

    def show_validation_errors(self, errors):
        for label in self.error_labels:
            label.destroy()

        self.error_labels.clear()

        if self.show_errors:
            for field, error_message in errors.items():
                error_text = f"{field}: {error_message} \t"
                error_label = ctk.CTkLabel(
                    self.container,
                    text=error_text,
                    width=500,
                    anchor="w",
                    fg_color="red",
                    corner_radius=5,
                )
                error_label.pack(expand=True, pady=10)
                self.error_labels.append(error_label)

    def __handle_submit(self):
        errors = self.__handle_validation()
        if not errors:
            data_to_insert = {
                "nombre": self.input_name.get(),
                "email": self.input_email.get(),
                "password": self.input_password.get(),
                "confirmedPassword": self.input_confirmed_password.get(),
            }
            try:
                self.auth_register_controller.register(data_to_insert)
                self.input_name.insert(0, "")
                self.input_email.insert(0, "")
                self.input_password.insert(0, "")
                self.input_confirmed_password.insert(0, "")
                self.controller.show_frame("Login")
            except Exception as ex:
                errors.update({"general": f"Error en el Registro {str(ex)}"})
                self.show_errors = True
        else:
            self.show_errors = True

        self.show_validation_errors(errors)

    def __handle_validation(self):
        error_to_send = {}
        email = self.input_email.get()
        name = self.input_name.get()
        password = self.input_password.get()
        confirmed_password = self.input_confirmed_password.get()
        if not name:
            error_to_send["Nombre"] = "Este campo es requerido"
        if email:
            email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
            if not re.match(email_pattern, email):
                error_to_send["email"] = "Debe tener un formato valido"
        else:
            error_to_send["Email"] = "Este campo es requerido"
        if not password:
            error_to_send["Contraseña"] = "Este campo es requerido"
        if not confirmed_password:
            error_to_send["Confirmar Contraseña"] = "Este campo es requerido"

        return error_to_send
