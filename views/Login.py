import re
import customtkinter as ctk

from controller.Auth.AuthLoginController import AuthLoginController
from controller.Auth.AuthCreateSessionController import AuthCreateSessionController
from lib.util_window import window_center
from views.Home import Home
from config import COLOR_ONE, COLOR_TWO


class Login(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.auth_login_create_controller = AuthLoginController()
        self.auth_create_session_contoller = AuthCreateSessionController()
        self.config_windows()
        self.create_widgets()
        self.show_errors = False
        self.error_labels = []

    def config_windows(self):
        self.title("Grupo Imnova - Login")
        # self.iconbitmap('../resources/logo.png')
        w, h = 1024, 600
        window_center(self, w, h)

    def create_widgets(self):
        """
        Crear los elementos de la interfaz
        """
        # screen
        self.container = ctk.CTkScrollableFrame(self)
        self.container.pack(fill=ctk.BOTH, expand=ctk.YES)

        self.title_primary = ctk.CTkLabel(self.container, text="Iniciar Sesión", font=("Roboto", 30))
        self.title_primary.pack(pady=20)

        # Input Email
        self.email_label = ctk.CTkLabel(self.container, text="Email", font=("Roboto", 15), anchor="w", width=500)
        self.email_label.pack(pady=5)
        self.email_input = ctk.CTkEntry(self.container, placeholder_text="Escribe tu email...", width=500)
        self.email_input.focus()
        self.email_input.pack()

        # Input Password
        self.password_label = ctk.CTkLabel(self.container, text="Contraseña", font=("Roboto", 15), anchor="w", width=500)
        self.password_label.pack(pady=5)
        self.password_input = ctk.CTkEntry(
            self.container,
            placeholder_text="Escribe tu contraseña...",
            width=500,
            show="*",
        )
        self.password_input.pack()

        # Button Submit
        self.submit_button = ctk.CTkButton(
            self.container,
            text="Iniciar Sesión",
            width=500,
            command=lambda: self._handle_submit(),
        )
        self.submit_button.pack(padx=10, pady=20)

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
            if user is None:
                print("Login failed")
            else:
                self.auth_create_session_contoller.new_session(user.get("id"))
                self.email_input.delete(0, ctk.END)
                self.email_input.delete(0, ctk.END)
                self.show_errors = False
                self.destroy()
                Home()
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
