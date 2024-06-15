import customtkinter as ctk

from config import COLOR_THREE, COLOR_BLUE_PRIMARY, COLOR_BLUE_SECONDARY
from controller.Auth.AuthRegisterController import AuthRegisterController
from controller.User.FindAllUserController import FindAllUserController
from controller.User.UpdateUserController import UpdateUserController
from controller.User.RemoveUserController import RemoveUserController
from sections.WindowComponent import WindowComponent
from tkinter import ttk


class Users(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.auth_find_all_user = FindAllUserController()
        self.auth_register_controller = AuthRegisterController()
        self.update_user_controller = UpdateUserController()
        self.remove_user_controller = RemoveUserController()
        self.widgets()
        self.widget_header()
        self.widget_body()
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

    def widgets(self):
        self.screen = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.screen.pack(expand=ctk.YES, fill=ctk.BOTH)

    def widget_header(self):
        # container
        self.header = ctk.CTkFrame(self.screen, fg_color="transparent")
        self.header.pack(side=ctk.TOP, fill=ctk.X, pady=10, padx=10)

        self.title = ctk.CTkLabel(
            self.header,
            text="Listado de Usuarios",
            font=("Roboto", 25),
            anchor="w",
            text_color="black",
        )
        self.title.pack(side=ctk.LEFT, fill=ctk.X)

        self.btn_refresh = ctk.CTkButton(
            self.header,
            text="  Refrescar",
            font=("Roboto", 12),
            command=self.refresh,
        )
        self.btn_refresh.pack(side=ctk.RIGHT, fill=ctk.X, padx=10)

        self.btn_create = ctk.CTkButton(
            self.header,
            text="  Crear nuevo usuario",
            font=("Roboto", 12),
            command=lambda: self.open_window_new_user(),
        )
        self.btn_create.pack(side=ctk.RIGHT, fill=ctk.X)

    def widget_body(self):
        # container
        self.container = ctk.CTkScrollableFrame(self.screen, fg_color=COLOR_THREE)
        self.container.pack(
            side=ctk.TOP, fill=ctk.BOTH, expand=ctk.YES, padx=10, pady=10
        )

        style = ttk.Style()
        style.configure(
            "Custom.Treeview",
            background=COLOR_THREE,
            foreground="black",
            rowheight=25,
            fieldbackground=COLOR_THREE,
            borderwidth=0,
        )
        style.configure(
            "Custom.Treeview.Heading",
            background=COLOR_BLUE_PRIMARY,
            foreground="black",
            font=("Roboto", 12, "bold"),
        )
        style.map(
            "Custom.Treeview.Heading",
            background=[
                ("active", COLOR_BLUE_SECONDARY),
                ("!active", COLOR_BLUE_PRIMARY),
            ],
            foreground=[("active", "white"), ("!active", "white")],
        )

        # table
        self.table = ttk.Treeview(
            self.container,
            style="Custom.Treeview",
            columns=("ID", "Nombre", "Cédula", "Rol", "Email"),
            show="headings",
            height=300,
        )
        self.table.heading("ID", text="ID")
        self.table.heading("Nombre", text="Nombre")
        self.table.heading("Cédula", text="Cédula")
        self.table.heading("Rol", text="Rol")
        self.table.heading("Email", text="Email")
        self.table.pack(padx=10, fill=ctk.BOTH, expand=ctk.YES)

        # Configurar columnas y centrado de texto
        self.table.column("ID", anchor="center")
        self.table.column("Nombre", anchor="center")
        self.table.column("Cédula", anchor="center")
        self.table.column("Rol", anchor="center")
        self.table.column("Email", anchor="center")

        # insert table
        users = self.auth_find_all_user.find_all()
        for i in range(len(users)):
            self.table.insert(
                parent="",
                index=0,
                values=(
                    users[i].get("id"),
                    users[i].get("name"),
                    users[i].get("dni"),
                    users[i].get("role"),
                    users[i].get("email"),
                ),
            )

        self.table.bind("<Button-1>", self.on_row_click)

    def open_window_new_user(self):
        self.window_modal = WindowComponent(
            self.options,
            self.auth_register_controller,
            "Crear un nuevo usuario",
            "create",
            None,
            None,
        )
        self.window_modal.grab_set()
        self.window_modal.protocol("WM_DELETE_WINDOW", self.close_window_modal)

    def on_row_click(self, event):
        item = self.table.identify_row(event.y)
        if item:
            values = self.table.item(item, "values")
            if values:
                data = {
                    "id": values[0],
                    "name": values[1],
                    "dni": values[2],
                    "role": values[3],
                    "email": values[4],
                }
                self.window_modal = WindowComponent(
                    self.options,
                    self.update_user_controller,
                    "Actualizar el usuario",
                    "update",
                    data,
                    self.remove_user_controller,
                )
                self.window_modal.grab_set()
                self.window_modal.protocol("WM_DELETE_WINDOW", self.close_window_modal)

    def refresh(self):
        self.__clear_widgets(self.screen)
        self.__render_data()

    def close_window_modal(self):
        self.__clear_widgets(self.screen)
        self.__render_data()
        self.window_modal.grab_release()
        self.window_modal.destroy()

    def __clear_widgets(self, widget):
        for w in widget.winfo_children():
            w.destroy()

    def __render_data(self):
        self.widget_header()
        self.widget_body()
