import customtkinter as ctk

from controller.Address.CreateAddressController import CreateAddressController
from controller.Address.UpdateAddressController import UpdateAddressController
from controller.Address.RemoveAddressController import RemoveAddressController
from controller.Address.GetAllAddressController import GetAllAddressController
from controller.User.FindUserController import FindUserController
from config import COLOR_THREE, COLOR_BLUE_PRIMARY, COLOR_BLUE_SECONDARY
from sections.WindowComponent import WindowComponent
from tkinter import ttk


class Address(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.options = [
            {"name": "name", "label": "Nombre", "type": "entry"},
            {"name": "city", "label": "Ciudad", "type": "entry"},
            {"name": "country", "label": "País", "type": "entry"},
            {"name": "state", "label": "Estado", "type": "entry"},
            {"name": "street", "label": "Calle", "type": "entry"},
            {"name": "postal_code", "label": "Código Postal", "type": "entry"},
            {"name": "location", "label": "Municipio/Localidad", "type": "entry"},
            {"name": "department", "label": "Urbanización/Departamento/Casa", "type": "entry"},
        ]
        self.create_address_controller = CreateAddressController()
        self.update_address_controller = UpdateAddressController()
        self.remove_address_controller = RemoveAddressController()
        self.get_all_address_controller = GetAllAddressController()
        self.find_user_controller = FindUserController()
        self.widgets()
        self.widget_header()
        self.widget_body()

    def widgets(self):
        self.screen = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.screen.pack(expand=ctk.YES, fill=ctk.BOTH)

    def widget_header(self):
        # container
        self.header = ctk.CTkFrame(self.screen, fg_color="transparent")
        self.header.pack(side=ctk.TOP, fill=ctk.X, pady=10, padx=10)

        self.title = ctk.CTkLabel(
            self.header,
            text="Listado de Direcciones",
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
            text="  Crear Dirección",
            font=("Roboto", 12),
            command=self.open_window_new_address,
        )
        self.btn_create.pack(side=ctk.RIGHT, fill=ctk.X)

    def widget_body(self):
        # container
        self.container = ctk.CTkScrollableFrame(self.screen, fg_color="transparent")
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
            columns=(
                "ID",
                "Nombre",
                "Dirección Principal"
            ),
            show="headings",
            height=35
        )
        self.table.heading("ID", text="ID")
        self.table.heading("Nombre", text="Nombre")
        self.table.heading("Dirección Principal", text="Dirección Principal")
        self.table.pack(padx=10, expand=ctk.YES, fill=ctk.BOTH)

        # Configurar columnas y centrado de texto
        self.table.column("ID", anchor="center")
        self.table.column("Nombre", anchor="center")
        self.table.column("Dirección Principal", anchor="center")

        # insert table
        data = self.get_all_address_controller.find_all()
        if data:
            for i in range(len(data)):
                self.table.insert(
                    parent="",
                    index=0,
                    values=(
                        data[i].get("id"),
                        data[i].get("name"),
                        data[i].get('main_address'),
                        data[i].get("city"),
                        data[i].get("country"),
                        data[i].get("state"),
                        data[i].get("street"),
                        data[i].get("postal_code"),
                        data[i].get("location"),
                        data[i].get('department')
                    ),
                )
            self.table.bind("<Button-1>", self.on_row_click)

    def on_row_click(self, event):
        item = self.table.identify_row(event.y)
        if item:
            values = self.table.item(item, "values")
            if values:
                data = {
                    "id": values[0],
                    "name": values[1],
                    "city": values[3],
                    "country": values[4],
                    "state": values[5],
                    "street": values[6],
                    "postal_code": values[7],
                    "location": values[8],
                    "department": values[9]
                }
                self.window_modal = WindowComponent(
                    self.options,
                    self.update_address_controller,
                    "Actualizar Dirección",
                    "update",
                    data,
                    self.remove_address_controller,
                    height=800
                )
                self.window_modal.grab_set()
                self.window_modal.protocol("WM_DELETE_WINDOW", self.close_window_modal)

    def open_window_new_address(self):
        self.window_modal = WindowComponent(
            self.options,
            self.create_address_controller,
            "Crear Nueva Dirección",
            "create",
            None,
            None,
            height=700
        )
        self.window_modal.grab_set()
        self.window_modal.protocol("WM_DELETE_WINDOW", self.close_window_modal)

    def refresh(self):
        self.__clear_widgets(self.screen)
        self.__render_data()

    def __clear_widgets(self, widget):
        for w in widget.winfo_children():
            w.destroy()

    def close_window_modal(self):
        self.__clear_widgets(self.screen)
        self.__render_data()
        self.window_modal.grab_release()
        self.window_modal.destroy()

    def __render_data(self):
        self.widget_header()
        self.widget_body()

    def __get_user_name(self, id):
        user = self.find_user_controller.find_user(id)
        return user.get('name')

