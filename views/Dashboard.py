import customtkinter as ctk
from controller.Auth.AuthCloseSessionController import AuthCloseSessionController
from config import WHITE, GRAY, BLACK, SLATE700, SLATE800
from lib import navigation


class Dashboard(ctk.CTk):
    """
    Frame para el Profile
    """

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.opciones_de_navegacion = navigation.NAVIGATION
        self.session_close_controller = AuthCloseSessionController()
        self.create_widgets()
        self.widget_superior_config()
        self.widget_lateral_config()
        self.widget_principal_config()

    def create_widgets(self):
        """
        Crea los elementos de la interfaz
        """
        # Barra Superior
        self.widget_superior = ctk.CTkFrame(
            self, height=50, fg_color=SLATE800, bg_color=SLATE800
        )
        self.widget_superior.pack(side=ctk.TOP, fill=ctk.BOTH, expand=ctk.NO)

        # Barra Lateral
        self.widget_lateral = ctk.CTkFrame(
            self, height=200, fg_color=SLATE800, bg_color=SLATE800
        )
        self.widget_lateral.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=ctk.NO)

        # Cuerpo
        self.widget_principal = ctk.CTkFrame(self, height=200, fg_color=GRAY)
        self.widget_principal.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=ctk.YES)

    def widget_superior_config(self):
        """
        Crea los elementos de la barra superior
        """
        font_awesome = ctk.CTkFont(family="FontAwesome", size=20)

        # Etiqueta Titulo
        self.label_titulo = ctk.CTkLabel(
            self.widget_superior,
            text="Bienvendio a Grupo Imnova!",
            font=("Roboto", 16),
            pady=10,
            padx=10,
            width=16,
        )
        self.label_titulo.pack(side=ctk.LEFT)

        self.btn_cerrar_sesion = ctk.CTkButton(
            self.widget_superior,
            text="  ",
            font=font_awesome,
            fg_color="transparent",
            bg_color="transparent",
            hover_color="red",
            width=40,
            command=lambda: self.logout(),
        )
        self.btn_cerrar_sesion.pack(side=ctk.RIGHT, padx=10)

        self.btn_profile_config = ctk.CTkButton(
            self.widget_superior,
            text="  ",
            font=font_awesome,
            fg_color="transparent",
            bg_color="transparent",
            hover_color="blue",
            width=40,
            command=lambda: self.controller.show_frame("Profile"),
        )
        self.btn_profile_config.pack(side=ctk.RIGHT)

    def widget_lateral_config(self):
        """
        Crea los elementos de la barra lateral
        """
        # Menu
        for i in range(len(self.opciones_de_navegacion)):
            self.btn_menu = ctk.CTkButton(
                self.widget_lateral,
                text=self.opciones_de_navegacion[i],
                font=("Roboto", 16),
                fg_color="transparent",
                bg_color="transparent",
                height=40,
                width=200,
                command=lambda: self.controller.show_frame(
                    self.opciones_de_navegacion[i]
                ),
            )
            self.btn_menu.pack(side=ctk.TOP, fill=ctk.X, pady=10)

    def widget_principal_config(self):
        """
        Crea los elementos del cuerpo principal
        """
        self.widget_principal_profile = ctk.CTkScrollableFrame(
            self.widget_principal, fg_color="transparent"
        )
        self.widget_principal_profile.pack(
            fill=ctk.BOTH, expand=ctk.YES, padx=10, pady=10
        )

    def logout(self):
        self.session_close_controller.close_session()
        self.controller.show_frame("Login")
