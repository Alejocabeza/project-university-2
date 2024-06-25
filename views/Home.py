import fontawesome as fa
import customtkinter as ctk

from views.Users import Users
from views.Address import Address
from views.Clients import Clients
from views.Profile import Profile
from views.Project import Project
from views.Employee import Employee
from lib.navigation import NAVIGATION
from views.Dashboard import Dashboard
from config import COLOR_ONE, COLOR_TWO
from lib.util_window import window_center
from views.ClientOffice import ClientOffice
from controller.User.GetUserController import GetUserController
from controller.Auth.AuthCloseSessionController import AuthCloseSessionController


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
        self.resizable(False, False)
        # self.iconbitmap('../resources/logo.png')
        w, h = 1440, 800
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
            padx=0,
            width=16,
            anchor=ctk.W,
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
        width = 50
        height = 40
        font_awesome = ctk.CTkFont(family="FontAwesome", size=20)

        # Menu Buttons
        self.buttonDashboard = ctk.CTkButton(self.widget_left, anchor="center")
        self.buttonClients = ctk.CTkButton(self.widget_left, anchor="center")
        self.buttonAddress = ctk.CTkButton(self.widget_left, anchor="center")
        self.buttonUsers = ctk.CTkButton(self.widget_left, anchor="center")
        self.buttonClientOffice = ctk.CTkButton(self.widget_left, anchor="center")
        self.buttonEmployee = ctk.CTkButton(self.widget_left, anchor="center")
        self.buttonProject = ctk.CTkButton(self.widget_left, anchor="center")

        # icons
        house_icon = fa.icons["warehouse"]
        users_icon = fa.icons["users"]
        address_icon = fa.icons["location-arrow"]
        office_icon = fa.icons["building"]
        client_icon = fa.icons["fire"]
        employee_icon = fa.icons["user-plus"]
        project_icon = fa.icons["project-diagram"]

        buttons_info = [
            (house_icon, self.buttonDashboard, self.open_dashboard),
            (users_icon, self.buttonUsers, self.open_users),
            (address_icon, self.buttonAddress, self.open_address),
            (office_icon, self.buttonClientOffice, self.open_client_office),
            (client_icon, self.buttonClients, self.open_clients),
            (employee_icon, self.buttonEmployee, self.open_employee),
            (project_icon, self.buttonProject, self.open_projects),
        ]

        for text, button, command in buttons_info:
            if (
                text == "Usuarios"
                and self.auth_get_data_controller.get_user_data().get("role") != "admin"
            ):
                continue
            self.config_btn_menu(button, text, font_awesome, width, height, command)

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

    def open_client_office(self):
        self.clear_widgets(self.widget_body)
        ClientOffice(self.widget_body)

    def open_employee(self):
        self.clear_widgets(self.widget_body)
        Employee(self.widget_body)

    def open_projects(self):
        self.clear_widgets(self.widget_body)
        Project(self.widget_body)

    def clear_widgets(self, widget):
        for widget in widget.winfo_children():
            widget.destroy()

    def config_btn_menu(self, button, text, font_awesome, width, height, command):
        button.configure(
            text=f" {text}   ",
            font=font_awesome,
            width=width,
            height=height,
            command=command,
            fg_color="transparent",
            bg_color="transparent",
        )
        button.pack(side=ctk.TOP, pady=5, padx=10)
