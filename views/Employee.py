import customtkinter as ctk
from tkinter import ttk

from controller.Employee.CreateEmployeeController import CreateEmployeeController
from controller.Employee.GetAllEmployeeController import GetAllEmployeeController
from controller.Employee.RemoveEmployeeController import RemoveEmployeeController
from controller.Employee.UpdateEmployeeController import UpdateEmployeeController
from sections.WindowComponent import WindowComponent
from config import COLOR_THREE, COLOR_BLUE_PRIMARY, COLOR_BLUE_SECONDARY


class Employee(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_employee_controller = CreateEmployeeController()
        self.update_employee_controller = UpdateEmployeeController()
        self.remove_employee_controller = RemoveEmployeeController()
        self.get_all_employee_controller = GetAllEmployeeController()
        self.widgets()
        self.widget_header()
        self.widget_body()
        self.window_modal = None
        self.options = [
            {"name": "firstname", "label": "Nombre", "type": "entry"},
            {"name": "lastname", "label": "Apellido", "type": "entry"},
            {"name": "dni", "label": "Cédula/RIF", "type": "entry"},
            {"name": "email", "label": "Email", "type": "entry"},
            {"name": "phone", "label": "Teléfono", "type": "entry"},
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
            text="Operario",
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
            text="  Crear un operario",
            font=("Roboto", 12),
            command=self.open_window_new_employee,
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
            columns=("ID", "firstname", "lastname", "dni", "email", "phone"),
            show="headings",
            height=35,
        )

        self.table.heading("ID", text="ID")
        self.table.heading("firstname", text="Nombre")
        self.table.heading("lastname", text="Apellido")
        self.table.heading("dni", text="Cedula/RIF")
        self.table.heading("email", text="Email")
        self.table.heading("phone", text="Telefono")
        self.table.pack(padx=10, fill=ctk.X, expand=ctk.YES)

        # Configurar columnas y centrado de texto
        self.table.column("ID", anchor="center")
        self.table.column("firstname", anchor="center")
        self.table.column("lastname", anchor="center")
        self.table.column("dni", anchor="center")
        self.table.column("email", anchor="center")
        self.table.column("phone", anchor="center")

        # insert table
        data = self.get_all_employee_controller.find_all()
        if data:
            for item in data:
                self.table.insert(
                    parent="",
                    index=0,
                    values=(
                        item.get("id"),
                        item.get("firstname"),
                        item.get("lastname"),
                        item.get("dni"),
                        item.get("email"),
                        item.get("phone"),
                    ),
                )

        self.table.bind("<Button-1>", self.on_row_click)

    def open_window_new_employee(self):
        self.window_modal = WindowComponent(
            self.options,
            self.create_employee_controller,
            "Crear un nuevo Operario",
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
                    "firstname": values[1],
                    "lastname": values[2],
                    "dni": values[3],
                    "email": values[4],
                    "phone": values[5],
                }
                self.window_modal = WindowComponent(
                    self.options,
                    self.update_employee_controller,
                    "Actualizar Operario",
                    "update",
                    data,
                    self.remove_employee_controller,
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
