import customtkinter as ctk

from controller.Auth.AuthCloseSessionController import AuthCloseSessionController
from controller.User.GetUserController import GetUserController
from lib.util_window import window_center
from lib.navigation import NAVIGATION
from config import COLOR_ONE, COLOR_TWO
from views.Profile import Profile
from views.Dashboard import Dashboard
from views.Clients import Clients
from views.Address import Address

# from views.Projects import Projects
# from views.Reports import Reports
from views.Users import Users


class Home(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.option_navigations = NAVIGATION
        self.session_close_controller = AuthCloseSessionController()
        self.auth_get_data_controller = GetUserController()
        self.config_windows()
        self.create_widgets()
        self.widget_top_config()
        self.widget_left_config()
        self.widget_body_config()

    def config_windows(self):
        self.title("Grupo Imnova")
        # self.iconbitmap('../resources/logo.png')
        self.resizable(False, False)
        w, h = 1200, 600
        window_center(self, w, h)
    def create_widgets(self):
        """
        Crea los elementos de la interfaz
        """
        # Barra Superior
        self.widget_top = ctk.CTkFrame(
            self, height=100, fg_color=COLOR_TWO, bg_color=COLOR_TWO
        )
        self.widget_top.pack(side=ctk.TOP, fill=ctk.BOTH, expand=ctk.NO)

        # Barra Lateral
        self.widget_left = ctk.CTkFrame(
            self, height=200, fg_color=COLOR_TWO, bg_color=COLOR_TWO
        )
        self.widget_left.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=ctk.NO)

        # Cuerpo
        self.widget_body = ctk.CTkFrame(self, height=200, fg_color=COLOR_ONE)
        self.widget_body.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=ctk.YES)

    def widget_top_config(self):
        """
        Crea los elementos de la barra superior
        """
        font_awesome = ctk.CTkFont(family="FontAwesome", size=20)
        self.label_title = ctk.CTkLabel(
            self.widget_top,
            text=f"Bienvenido {self.auth_get_data_controller.get_user_data().get('name')}",
            font=("Roboto", 16),
            pady=10,
            padx=10,
            width=16,
        )
        self.label_title.pack(side=ctk.LEFT, padx=20)

        # self.btn_close_session = ctk.CTkButton(
        #     self.widget_top,
        #     text="  ",
        #     font=font_awesome,
        #     fg_color="transparent",
        #     bg_color="transparent",
        #     hover_color="red",
        #     width=40,
        #     command=self.logout,
        # )
        # self.btn_close_session.pack(side=ctk.RIGHT, padx=10)

        self.btn_profile_config = ctk.CTkButton(
            self.widget_top,
            text="  ",
            font=font_awesome,
            fg_color="transparent",
            bg_color="transparent",
            hover_color="blue",
            width=40,
            command=lambda: self.init_profile_widget(),
        )
        self.btn_profile_config.pack(side=ctk.RIGHT)

    def widget_left_config(self):
        """
        Crea los elementos de la barra lateral
        """
        width = 200
        height = 40
        font_awesome = ctk.CTkFont(family="FontAwesome", size=15)

        # Menu Buttons
        self.buttonDashboard = ctk.CTkButton(self.widget_left)
        self.buttonClients = ctk.CTkButton(self.widget_left)
        # self.buttonProjects = ctk.CTkButton(self.widget_left)
        # self.buttonReports = ctk.CTkButton(self.widget_left)
        self.buttonAddress = ctk.CTkButton(self.widget_left)
        self.buttonUsers = ctk.CTkButton(self.widget_left)

        buttons_info = [
            ("Dashboard", "", self.buttonDashboard, self.open_dashboard),
            ("Clientes", "", self.buttonClients, self.open_clients),
            # ("Proyectos", "", self.buttonProjects, self.open_projects),
            # ("Reportes", "", self.buttonReports, self.open_reports),
            ("Direcciones", "", self.buttonAddress, self.open_address),
            ("Usuarios", "", self.buttonUsers, self.open_users),
        ]

        for text, icon, button, command in buttons_info:
            if (
                text == "Usuarios"
                and self.auth_get_data_controller.get_user_data().get("role") != "admin"
            ):
                continue
            self.config_btn_menu(
                button, text, icon, font_awesome, width, height, command
            )

    def widget_body_config(self):
        """
        Crea los elementos del cuerpo principal
        """
        self.widget_main_profile = ctk.CTkScrollableFrame(
            self.widget_body, fg_color="transparent"
        )
        self.widget_main_profile.pack(fill=ctk.BOTH, expand=ctk.YES, padx=10, pady=10)

    def logout(self):
        self.session_close_controller.close_session()
        self.destroy()
        Login()

    def init_profile_widget(self):
        self.clear_widgets(self.widget_body)
        Profile(self.widget_body)

    def open_dashboard(self):
        self.clear_widgets(self.widget_body)
        Dashboard(self.widget_body)

    def open_clients(self):
        self.clear_widgets(self.widget_body)
        Clients(self.widget_body)

    def open_users(self):
        self.clear_widgets(self.widget_body)
        Users(self.widget_body)

    def open_address(self):
        self.clear_widgets(self.widget_body)
        Address(self.widget_body)

    def clear_widgets(self, widget):
        for widget in widget.winfo_children():
            widget.destroy()

    def config_btn_menu(self, button, text, icon, font_awesome, width, height, command):
        button.configure(
            text=f"{icon}   {text}",
            font=font_awesome,
            width=width,
            height=height,
            command=command,
            fg_color="transparent",
            bg_color="transparent",
        )
        button.pack(side=ctk.TOP, pady=5, padx=10)
