import re
import fontawesome as fa
import customtkinter as ctk

from views.Home import Home
from config import ONE_COLOR, TWO_COLOR, THREE_COLOR, THREE_COLOR_HOVER
from lib.util_window import window_center
from controller.Auth.AuthLoginController import AuthLoginController
from controller.Auth.AuthCreateSessionController import AuthCreateSessionController


class Login(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.font_awesome = ctk.CTkFont(family="FontAwesome", size=20)
        self.auth_login_create_controller = AuthLoginController()
        self.auth_create_session_contoller = AuthCreateSessionController()
        self.config_windows()
        self.create_widgets()
        self.show_errors = False
        self.error_labels = []

    def config_windows(self):
        self.title("Grupo Imnova - Login")
        # self.iconbitmap('../resources/logo.png')
        w, h = 450, 600
        window_center(self, w, h)

    def create_widgets(self):
        """
        Crear los elementos de la interfaz
        """
        self.screen = ctk.CTkFrame(
            self, fg_color=TWO_COLOR, bg_color=TWO_COLOR, corner_radius=40
        )
        self.screen.pack(fill=ctk.BOTH, expand=ctk.YES)
        # screen
        self.container = ctk.CTkFrame(self.screen, fg_color="transparent")
        self.container.pack(fill=ctk.BOTH, expand=ctk.YES, pady=40, padx=40)

        self.title_primary = ctk.CTkLabel(
            self.container,
            text="Iniciar Sesión",
            font=("Roboto", 30),
            text_color=ONE_COLOR,
        )
        self.title_primary.pack(pady=20)

        # Input Email
        self.email_label = ctk.CTkLabel(
            self.container,
            text="Email",
            font=("Roboto", 18),
            text_color=ONE_COLOR,
            anchor="w",
            width=500,
        )
        self.email_label.pack(pady=5)
        self.email_input = ctk.CTkEntry(
            self.container, placeholder_text="Escribe tu email...", width=500, bg_color='transparent', fg_color='transparent', border_color='white', border_width=1
        )
        self.email_input.focus()
        self.email_input.pack()

        # Input Password
        self.password_label = ctk.CTkLabel(
            self.container,
            text="Contraseña",
            text_color=ONE_COLOR,
            font=("Roboto", 18),
            anchor="w",
            width=500,
        )
        self.password_label.pack(pady=5)
        self.password_input = ctk.CTkEntry(
            self.container,
            placeholder_text="Escribe tu contraseña...",
            width=500,
            bg_color='transparent',
            fg_color='transparent',
            border_color='white',
            border_width=1,
            show="*",
        )
        self.password_input.pack()

        # Button Submit
        self.submit_button = ctk.CTkButton(
            self.container,
            text="Iniciar Sesión",
            width=500,
            fg_color=THREE_COLOR,
            hover_color=THREE_COLOR_HOVER,
            command=self._handle_submit,
        )
        self.submit_button.pack(pady=20)

    def show_validation_errors(self, errors):
        for label in self.error_labels:
            label.destroy()

        self.error_labels.clear()

        if self.show_errors:
            for field, error_message in errors.items():
                error_text = f"{field}: {error_message} \t"
                error_label = ctk.CTkLabel(
                    self.screen,
                    text=error_text,
                    width=500,
                    anchor="w",
                    fg_color="red",
                    corner_radius=5,
                )
                error_label.pack(expand=ctk.NO, pady=10)
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
