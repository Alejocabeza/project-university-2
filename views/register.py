import customtkinter as ctk
from repository.UserRepository import UserRepository


class Register (ctk.CTkFrame):
    """
    Muestra el frame de Crear una Cuenta
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()
        self.user_repository= UserRepository()

    def create_widgets(self):
        """
        Crea los elementos de la interfaz
        """
        # screen
        self.screen = ctk.CTkFrame(self)
        self.screen.pack(fill=ctk.BOTH, expand=ctk.YES)

        self.container = ctk.CTkFrame(
            self.screen,
        )
        self.container.pack(fill=ctk.BOTH, expand=ctk.YES, pady=160, padx=240)

        self.title = ctk.CTkLabel(
            self.container, text="Crear una Cuenta", font=("Arial", 30)
        )
        self.title.pack(pady=20)

        # input Name
        self.input_name = ctk.CTkEntry(
            self.container, placeholder_text="Escribe aquí tu nombre...", width=500
        )
        self.input_name.pack(pady=5)

        # input Email
        self.input_email = ctk.CTkEntry(
            self.container, placeholder_text="Escribe aquí tu email...", width=500
        )
        self.input_email.pack(pady=5)

        # input Password
        self.input_password = ctk.CTkEntry(
            self.container,
            placeholder_text="Escribe tu contraseña...",
            width=500,
            show="*",
        )
        self.input_password.pack(pady=5)

        # input confirmed Password
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

    def __handle_submit(self):
        data_to_insert = {
            "nombre": self.input_name.get(),
            "email": self.input_email.get(),
            "password": self.input_password.get(),
            "confirmedPassword": self.input_confirmed_password.get(),
        }
        result = self.user_repository.register(data=data_to_insert)
        if result is False:
            print("Register failed")
        else:
            self.controller.show_frame("Login")
