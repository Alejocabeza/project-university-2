import customtkinter as ctk

from config import COLOR_THREE


class Clients(ctk.CTk):
    def __init__(self, parent):
        self.parent = parent
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
            text="Listado de Clientes",
            font=("Roboto", 25),
            anchor="w",
            text_color="black",
        )
        self.title.pack(side=ctk.LEFT, fill=ctk.X)

        self.btn_create = ctk.CTkButton(
            self.header, text="  Crear nuevo cliente", font=("Roboto", 12)
        )
        self.btn_create.pack(side=ctk.RIGHT, fill=ctk.X)

    def widget_body(self):
        # container
        self.container = ctk.CTkScrollableFrame(self.screen, fg_color=COLOR_THREE, height=300)
        self.container.pack(side=ctk.TOP, fill=ctk.BOTH, expand=ctk.YES, padx=10, pady=10)
