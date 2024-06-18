import os

# Plantilla para la vista
view_template = """
import customtkinter as ctk
from tkinter import ttk

from controller.{name}.Create{name}Controller import Create{name}Controller
from controller.{name}.GetAll{name}Controller import GetAll{name}Controller
from controller.{name}.Remove{name}Controller import Remove{name}Controller
from controller.{name}.Update{name}Controller import Update{name}Controller
from sections.WindowComponent import WindowComponent

class {name}(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.options = []
        self.create_{name_lower}_controller = Create{name}Controller()
        self.update_{name_lower}_controller = Update{name}Controller()
        self.remove_{name_lower}_controller = Remove{name}Controller()
        self.get_all_{name_lower}_controller = GetAll{name}Controller()
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
            text="{name}",
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
            text="  Add {name}",
            font=("Roboto", 12),
            command=self.open_window_new_{name_lower},
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
            background="white",
            foreground="black",
            rowheight=25,
            fieldbackground="white",
            borderwidth=0,
        )
        style.configure(
            "Custom.Treeview.Heading",
            background="blue",
            foreground="black",
            font=("Roboto", 12, "bold"),
        )
        style.map(
            "Custom.Treeview.Heading",
            background=[
                ("active", "lightblue"),
                ("!active", "blue"),
            ],
            foreground=[("active", "white"), ("!active", "white")],
        )

        # table
        self.table = ttk.Treeview(
            self.container,
            style="Custom.Treeview",
            columns=("ID"),
            show="headings",
            height=300,
        )
        self.table.heading("ID", text="ID")
        self.table.pack(padx=10, fill=ctk.BOTH, expand=ctk.YES)

        # Configurar columnas y centrado de texto
        self.table.column("ID", anchor="center")

        # insert table
        data = self.get_all_{name_lower}_controller.find_all()
        for item in data:
            self.table.insert(
                parent="",
                index=0,
                values=(
                    item.get("id"),
                ),
            )

        self.table.bind("<Button-1>", self.on_row_click)

    def open_window_new_{name_lower}(self):
        self.window_modal = WindowComponent(
            self.options,
            self.create_{name_lower}_controller,
            "Create new {name}",
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
                data = {{
                    "id": values[0],
                }}
                self.window_modal = WindowComponent(
                    self.options,
                    self.update_{name_lower}_controller,
                    "Update {name}",
                    "update",
                    data,
                    self.remove_{name_lower}_controller,
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
"""


def create_file(content, path):
    # Crear directorio si no existe
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)


# Crear un nuevo controlador
def create_view(name):
    view_name = name.capitalize()
    view_content = view_template.format(
        name=view_name,
        name_lower=name.lower(),
    )
    view_path = os.path.join("views", f"{view_name}.py")
    create_file(view_content, view_path)
