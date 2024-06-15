import customtkinter as ctk

from controller.Clients.CreateClientController import CreateClientController
from controller.Clients.GetAllClientController import GetAllClientController
from controller.Clients.RemoveClientController import RemoveClientController
from controller.Clients.UpdateClientController import UpdateClientController
from controller.Address.GetAllAddressController import GetAllAddressController
from controller.Address.FindAddressByIdController import FindAddressByIdController
from config import COLOR_THREE, COLOR_BLUE_PRIMARY, COLOR_BLUE_SECONDARY
from sections.WindowComponent import WindowComponent
from tkinter import ttk


class Clients(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_client_controller = CreateClientController()
        self.update_client_controller = UpdateClientController()
        self.remove_client_controller = RemoveClientController()
        self.get_all_client_controller = GetAllClientController()
        self.get_all_address_controller = GetAllAddressController()
        self.find_address_by_id = FindAddressByIdController()
        self.widgets()
        self.widget_header()
        self.widget_body()
        self.options = [
            {"name": "name", "label": "Nombre", "type": "entry"},
            {"name": "dni", "label": "DNI/RIF", "type": "entry"},
            {"name": "email", "label": "Email", "type": "entry"},
            {"name": "phone", "label": "Telefono", "type": "entry"},
            {
                "name": "type",
                "label": "Tipo de Cliente",
                "type": "combobox",
                "options": [
                    "Persona Natural",
                    "Persona Jurídica",
                    "Gubernamental",
                ],
            },
            {
                "name": "address",
                "label": "Dirección",
                "type": "combobox",
                "options": self.__get_address_all(),
            },
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
            text="  Crear Cliente",
            font=("Roboto", 12),
            command=self.open_window_new_client,
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
            columns=(
                "id",
                "name",
                "dni",
                "email",
                "phone",
                "type",
                "address",
            ),
            show="headings",
            height=500,
        )
        self.table.heading("id", text="ID")
        self.table.heading("name", text="Nombre")
        self.table.heading("dni", text="DNI/RIF")
        self.table.heading("email", text="Email")
        self.table.heading("phone", text="Telefono")
        self.table.heading("type", text="Tipo de Cliente")
        self.table.heading("address", text="Dirección")
        self.table.pack(padx=10, expand=ctk.YES, fill=ctk.BOTH)

        # Configurar columnas y centrado de texto
        self.table.column("id", anchor="center")
        self.table.column("name", anchor="center")
        self.table.column("dni", anchor="center")
        self.table.column("email", anchor="center")
        self.table.column("phone", anchor="center")
        self.table.column("type", anchor="center")
        self.table.column("address", anchor="center")

        # insert table
        data = self.get_all_client_controller.find_all()
        if data:
            for i in range(len(data)):
                type_client = self.__get_type_client(data[i].get("type"))
                address = self.__get_name_address(data[i].get("address"))
                self.table.insert(
                    parent="",
                    index=0,
                    values=(
                        data[i].get("id"),
                        data[i].get("name"),
                        data[i].get("dni"),
                        data[i].get("email"),
                        data[i].get("phone"),
                        type_client,
                        address,
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
                    "dni": values[2],
                    "email": values[3],
                    "phone": values[4],
                    "type": values[5],
                    "address": values[6],
                }
                self.window_modal = WindowComponent(
                    self.options,
                    self.update_client_controller,
                    "Actualizar Cliente",
                    "update",
                    data,
                    self.remove_client_controller,
                )
                self.window_modal.grab_set()
                self.window_modal.protocol("WM_DELETE_WINDOW", self.close_window_modal)

    def open_window_new_client(self):
        self.window_modal = WindowComponent(
            self.options,
            self.create_client_controller,
            "Crear Nuevo Cliente",
            "create",
            None,
            None,
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

    def __get_address_all(self):
        data_to_return = list()
        data = self.get_all_address_controller.find_all()
        if data:
            for address in data:
                data_to_return.append(address.get("name"))
        return data_to_return

    def __get_name_address(self, id):
        address = self.find_address_by_id.find_by_id(id)
        return address.get("name")

    def __get_type_client(self, type):
        match type:
            case "person":
                return "Persona Natural"
            case "company":
                return "Persona Jurídica"
            case 'government':
                return 'Gubernamental'
