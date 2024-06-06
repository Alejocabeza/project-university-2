import customtkinter as ctk
from repository.UserRepository import User
from config import BLUE, WHITE


# This class is used as the main window
class Login(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.user = User()
        self.create_widgets()

    def create_widgets(self):
        # screen
        self.screen = ctk.CTkFrame(self)
        self.screen.pack(fill=ctk.BOTH, expand=ctk.YES)

        # container
        self.container = ctk.CTkFrame(
            self.screen,
        )
        self.container.pack(fill=ctk.BOTH, expand=ctk.YES, pady=195, padx=240)

        self.title = ctk.CTkLabel(
            self.container, text="Iniciar Sesion", font=("Arial", 30)
        )
        self.title.pack(pady=20)

        # Input Email
        self.emailInput = ctk.CTkEntry(
            self.container, placeholder_text="Escribe tu email...", width=500
        )
        self.emailInput.pack()

        # Input Password
        self.passwordInput = ctk.CTkEntry(
            self.container,
            placeholder_text="Escribe tu contraseña...",
            width=500,
            show="*",
        )
        self.passwordInput.pack(pady=15)

        # Button Box
        self.buttonBox = ctk.CTkFrame(
            self.container, bg_color="transparent", fg_color="transparent"
        )
        self.buttonBox.pack(pady=8)

        # Button Register
        self.btnRegister = ctk.CTkButton(
            self.buttonBox,
            bg_color="transparent",
            fg_color="transparent",
            text="Aun no tienes cuenta?",
            command=lambda: self.controller.show_frame("Register"),
        )
        self.btnRegister.pack(side="left")

        # Button Submit
        self.btnSubmit = ctk.CTkButton(
            self.buttonBox,
            text="Iniciar Sesion",
            command=lambda: self._handleSubmit(
                self.emailInput.get(), self.passwordInput.get()
            ),
        )
        self.btnSubmit.pack(side="right", padx=8)

    def _handleSubmit(self, email, password):
        result = self.user.login(email, password)
        if result is None:
            print("Login failed")
        else:
            self.controller.show_frame("Dashboard")
