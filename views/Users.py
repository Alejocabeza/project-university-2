import customtkinter as ctk

from controller.Auth.AuthRegisterController import AuthRegisterController
from controller.User.FindAllUserController import FindAllUserController
from controller.User.UpdateUserController import UpdateUserController
from controller.User.RemoveUserController import RemoveUserController
from controller.User.FindUserByIdController import FindUserByIdController
from sections.TableModule import TableModule
from sections.HeaderModule import HeaderModule


class Users(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.auth_find_all_user = FindAllUserController()
        self.find_user_by_id = FindUserByIdController()
        self.auth_register_controller = AuthRegisterController()
        self.update_user_controller = UpdateUserController()
        self.remove_user_controller = RemoveUserController()
        self.options = [
            {"name": "name", "label": "Nombre", "type": "entry"},
            {"name": "email", "label": "Email", "type": "entry"},
            {
                "name": "role",
                "label": "Rol",
                "type": "combobox",
                "options": ["Usuario", "Administrador"],
            },
            {"name": "dni", "label": "Cedula", "type": "entry"},
            {"name": "password", "label": "Contraseña", "type": "entry"},
        ]
        self.widgets()
        self.widget_header()
        self.widget_body()

    def widgets(self):
        self.screen = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.screen.pack(expand=ctk.YES, fill=ctk.BOTH)

    def widget_header(self):
        # container
        HeaderModule(
            self.screen,
            "Usuarios",
            self.refresh,
            self.options,
            self.auth_register_controller,
        )

    def widget_body(self):
        data = self.auth_find_all_user.find_all()
        TableModule(
            self.screen,
            {
                "id": "ID",
                "name": "Nombre",
                "dni": "DNI/RIF",
                "role": "Rol",
                "email": "Email",
            },
            data,
            self.find_user_by_id,
            self.options,
            self.update_user_controller,
            self.remove_user_controller,
        )

    def refresh(self):
        self.__clear_widgets(self.screen)
        self.__render_data()

    def __clear_widgets(self, widget):
        for w in widget.winfo_children():
            w.destroy()

    def __render_data(self):
        self.widget_header()
        self.widget_body()
