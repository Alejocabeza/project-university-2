import os

# Plantilla para la vista
view_template = """
import customtkinter as ctk

from sections.TableModule import TableModule
from sections.HeaderModule import HeaderModule
from controller.{name}.Create{name}Controller import Create{name}Controller
from controller.{name}.GetAll{name}Controller import GetAll{name}Controller
from controller.{name}.Remove{name}Controller import Remove{name}Controller
from controller.{name}.Update{name}Controller import Update{name}Controller
from controller.{name}.Find{name}ByIdController import Find{name}ByIdController

class {name}(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_{name_lower}_controller = Create{name}Controller()
        self.update_{name_lower}_controller = Update{name}Controller()
        self.remove_{name_lower}_controller = Remove{name}Controller()
        self.get_all_{name_lower}_controller = GetAll{name}Controller()
        self.find_{name_lower}_by_id_controller = Find{name}ByIdController()
        self.options = {options}
        self.widgets()
        self.widget_header()
        self.widget_body()
        self.window_modal = None

    def widgets(self):
        self.screen = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.screen.pack(expand=ctk.YES, fill=ctk.BOTH)

    def widget_header(self):
        # container
        HeaderModule(
            self.screen, 
            "{name_spanish}",
            self.refresh,
            self.options,
            self.create_{name_lower}_controller
        )

    def widget_body(self):
        # container
        data = self.get_all_{name_lower}_controller.find_all()
        TableModule(
            self.screen,
            {"id": "ID"},
            data,
            self.find_{name_lower}_by_id_controller,
            self.options,
            self.update_{name_lower}_controller,
            self.remove_{name_lower}_controller
        )

    def refresh(self):
        self.__clear_widgets(self.screen)
        self.__render_data()

    def close_window_modal(self):
        self.__clear_widgets(self.screen)
        self.__render_data()

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
def create_view(name, options, name_spanish):
    view_name = name.capitalize()
    view_content = view_template.format(
        name=view_name,
        name_lower=name.lower(),
        options=options,
        name_spanish=name_spanish,
    )
    view_path = os.path.join("views", f"{view_name}.py")
    create_file(view_content, view_path)
