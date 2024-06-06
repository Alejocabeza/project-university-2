import customtkinter as ctk
from tkinter import font
from repository.UserRepository import User


class Register(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.userService = User()
        self.create_widget()

    def create_widget(self):
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
        self.nameInput = ctk.CTkEntry(
            self.container, placeholder_text="Escribe aquí tu nombre...", width=500
        )
        self.nameInput.pack(pady=5)

        # input Email
        self.emailInput = ctk.CTkEntry(
            self.container, placeholder_text="Escribe aquí tu email...", width=500
        )
        self.emailInput.pack(pady=5)

        # input Password
        self.inputPassword = ctk.CTkEntry(
            self.container,
            placeholder_text="Escribe tu contraseña...",
            width=500,
            show="*",
        )
        self.inputPassword.pack(pady=5)

        # input confirmed Password
        self.inputPasswordConfirmed = ctk.CTkEntry(
            self.container,
            placeholder_text="Confirma tu contraseña...",
            width=500,
            show="*",
        )
        self.inputPasswordConfirmed.pack(pady=5)

        # Button Box
        self.buttonBox = ctk.CTkFrame(
            self.container, bg_color="transparent", fg_color="transparent"
        )
        self.buttonBox.pack(pady=10)

        # Button Register
        self.btnRegister = ctk.CTkButton(
            self.buttonBox,
            bg_color="transparent",
            fg_color="transparent",
            text="Ya tienes una cuenta?",
            command=lambda: self.controller.show_frame("Login"),
        )
        self.btnRegister.pack(side="left")

        # Button Submit
        self.btnSubmit = ctk.CTkButton(
            self.buttonBox,
            text="Craer Cuenta",
            command=lambda: self.__handleSubmit(),
        )
        self.btnSubmit.pack(side="right", padx=8)

    def __handleSubmit(self):
        data_to_insert = {
            "nombre": self.nameInput.get(),
            "email": self.emailInput.get(),
            "password": self.inputPassword.get(),
            "confirmedPassword": self.inputPasswordConfirmed.get(),
        }
        result = self.userService.register(data=data_to_insert)
        if result is False:
            print("Register failed")
        else:
            self.controller.show_frame("Login")
