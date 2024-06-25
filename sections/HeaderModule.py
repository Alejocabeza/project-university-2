import fontawesome as fa
import customtkinter as ctk

from config import COLOR_TWO
from sections.WindowComponent import WindowComponent


class HeaderModule(ctk.CTkFrame):
    def __init__(
        self, parent, name, refresh, options, ctrl_create, height=600, width=450
    ):
        super().__init__(parent)
        self.parent = parent
        self.name = name
        self.refresh = refresh
        self.options = options
        self.ctrl_create = ctrl_create
        self.height = height
        self.width = width
        self.header_widget()

    def header_widget(self):
        font_awesome = ctk.CTkFont(family="FontAwesome", size=20)
        self.header = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.header.pack(side=ctk.TOP, fill=ctk.X, pady=10, padx=10)

        self.title = ctk.CTkLabel(
            self.header,
            text=f"Listado de {self.name}",
            font=font_awesome,
            anchor="w",
            text_color="black",
        )
        self.title.pack(side=ctk.LEFT, fill=ctk.X)

        self.btn_refresh = ctk.CTkButton(
            self.header,
            text=f" {fa.icons['arrow-alt-circle-right']}   ",
            font=font_awesome,
            command=self.refresh,
            bg_color="transparent",
            fg_color=COLOR_TWO,
            anchor="center",
            width=40,
        )
        self.btn_refresh.pack(side=ctk.RIGHT, padx=10, fill=ctk.X)

        self.btn_create = ctk.CTkButton(
            self.header,
            text=f" {fa.icons['plus']}  ",
            font=font_awesome,
            command=lambda: self.open_modal(),
            bg_color="transparent",
            fg_color=COLOR_TWO,
            anchor="center",
            width=40,
        )
        self.btn_create.pack(side=ctk.RIGHT, fill=ctk.X)

    def open_modal(self):
        self.modal = WindowComponent(
            self.options,
            self.ctrl_create,
            f"Agregar {self.name}",
            "create",
            None,
            None,
            self.width,
            self.height,
        )
        self.modal.grab_set()
        self.modal.protocol("WM_DELETE_WINDOW", self.close_modal)

    def close_modal(self):
        self.refresh()
        self.modal.grab_release()
        self.modal.destroy()
