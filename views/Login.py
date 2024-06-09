import re
import customtkinter as ctk
from controller.Auth.AuthLoginController import AuthLoginController
from controller.Auth.AuthCreateSessionController import AuthCreateSessionController


class Login(ctk.CTkFrame):
    """
    Frame de inicio de sesión
    """

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.auth_login_create_controller = AuthLoginController()
        self.auth_create_session_contoller = AuthCreateSessionController()
        self.create_widgets()
        self.show_errors = False
        self.error_labels = []

    def create_widgets(self):
        """
        Crear los elementos de la interfaz
        """
        # screen
        self.screen = ctk.CTkScrollableFrame(self)
        self.screen.pack(fill=ctk.BOTH, expand=ctk.YES)

        # container
        self.container = ctk.CTkFrame(
            self.screen,
        )
        self.container.pack(fill=ctk.BOTH, expand=ctk.YES)

        self.title = ctk.CTkLabel(
            self.container, text="Iniciar Sesión", font=("Arial", 30)
        )
        self.title.pack(pady=20)

        # Input Email
        self.email_label = ctk.CTkLabel(
            self.container, text="Email", font=("Arial", 15), anchor="w", width=500
        )
        self.email_label.pack(pady=5)
        self.email_input = ctk.CTkEntry(
            self.container, placeholder_text="Escribe tu email...", width=500
        )
        self.email_input.focus()
        self.email_input.pack()

        # Input Password
        self.password_label = ctk.CTkLabel(
            self.container, text="Contraseña", font=("Arial", 15), anchor="w", width=500
        )
        self.password_label.pack(pady=5)
        self.password_input = ctk.CTkEntry(
            self.container,
            placeholder_text="Escribe tu contraseña...",
            width=500,
            show="*",
        )
        self.password_input.pack()

        # Button Box
        self.container_buttons = ctk.CTkFrame(
            self.container, bg_color="transparent", fg_color="transparent"
        )
        self.container_buttons.pack(pady=20)

        # Button Register
        self.register_button = ctk.CTkButton(
            self.container_buttons,
            bg_color="transparent",
            fg_color="transparent",
            text="Aun no tienes cuenta?",
            command=lambda: self.controller.show_frame("Register"),
        )
        self.register_button.pack(side="left")

        # Button Submit
        self.submit_button = ctk.CTkButton(
            self.container_buttons,
            text="Iniciar Sesión",
            command=lambda: self._handle_submit(),
        )
        self.submit_button.pack(side="right", padx=8)

    def show_validation_errors(self, errors):
        for label in self.error_labels:
            label.destroy()

        self.error_labels.clear()

        if self.show_errors:
            for field, error_message in errors.items():
                error_text = f"{field}: {error_message} \t"
                error_label = self.error_box = ctk.CTkLabel(
                    self.container,
                    text=error_text,
                    width=500,
                    anchor="w",
                    fg_color="red",
                    corner_radius=5,
                )
                error_label.pack(expand=True, pady=10)
                self.error_labels.append(error_label)

    def _handle_submit(self):
        errors = self.__handle_validation()
        email = self.email_input.get()
        password = self.password_input.get()
        if not errors:
            user = self.auth_login_create_controller.login(email, password)
            print(user)
            if user is None:
                print("Login failed")
            else:
                self.auth_create_session_contoller.new_session(user.get("id"))
                self.email_input.delete(0, ctk.END)
                self.email_input.delete(0, ctk.END)
                self.show_errors = False
                self.controller.show_frame("Dashboard")
        else:
            self.show_errors = True

        self.show_validation_errors(errors)

    def __handle_validation(self):
        error_to_send = {}
        email = self.email_input.get()
        password = self.password_input.get()
        if email:
            email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
            if not re.match(email_pattern, email):
                error_to_send["Email"] = "Debe tener un formato valido"
        else:
            error_to_send["Email"] = "Este campo es requerido"
        if not password:
            error_to_send["Contraseña"] = "Este campo es requerido"

        return error_to_send
