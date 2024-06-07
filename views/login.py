import customtkinter as ctk
from repository.UserRepository import UserRepository
from repository.SessionRepository import SessionRepository

class Login(ctk.CTkFrame):
    """
    Frame de inicio de sesión
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.user_repository = UserRepository()
        self.session_repository = SessionRepository()
        self.create_widgets()

    def create_widgets(self):
        """
        Crear los elementos de la interfaz
        """
        # screen
        self.screen = ctk.CTkFrame(self)
        self.screen.pack(fill=ctk.BOTH, expand=ctk.YES)

        # container
        self.container = ctk.CTkFrame(
            self.screen,
        )
        self.container.pack(fill=ctk.BOTH, expand=ctk.YES, pady=195, padx=240)

        self.title = ctk.CTkLabel(
            self.container, text="Iniciar Sesión", font=("Arial", 30)
        )
        self.title.pack(pady=20)

        # Input Email
        self.email_input = ctk.CTkEntry(
            self.container, placeholder_text="Escribe tu email...", width=500
        )
        self.email_input.pack()

        # Input Password
        self.password_input = ctk.CTkEntry(
            self.container,
            placeholder_text="Escribe tu contraseña...",
            width=500,
            show="*",
        )
        self.password_input.pack(pady=15)

        # Button Box
        self.container_buttons = ctk.CTkFrame(
            self.container, bg_color="transparent", fg_color="transparent"
        )
        self.container_buttons.pack(pady=8)

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
            command=lambda: self._handle_submit(
                self.email_input.get(), self.password_input.get()
            ),
        )
        self.submit_button.pack(side="right", padx=8)

    def _handle_submit(self, email, password):
        result = self.user_repository.login(email, password)
        if result is None:
            print("Login failed")
        else:
            self.session_repository.create_session(result)
            self.controller.show_frame("Dashboard")
