import fontawesome as fa
import customtkinter as ctk
from tkinter import ttk

from config import COLOR_THREE, COLOR_TWO
from sections.WindowComponent import WindowComponent


class TableModule(ctk.CTkFrame):
    def __init__(
        self,
        parent,
        headers,
        data,
        function_find,
        options,
        update_controller,
        remove_controller,
        height=600,
        width=450,
    ):
        super().__init__(parent)
        self.parent = parent
        self.headers = headers
        self.data = data
        self.function_find = function_find
        self.options = options
        self.update_controller = update_controller
        self.remove_controller = remove_controller
        self.height = height
        self.width = width
        self.widget()

    def widget(self):
        self.container = ctk.CTkScrollableFrame(self.parent, fg_color="transparent")
        self.container.pack(side=ctk.TOP, fill=ctk.BOTH, expand=ctk.YES, padx=5, pady=5)

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
            background=COLOR_TWO,
            foreground="black",
            font=("Roboto", 12, "bold"),
        )
        style.map(
            "Custom.Treeview.Heading",
            background=[
                ("active", COLOR_TWO),
                ("!active", COLOR_TWO),
            ],
            foreground=[("active", "white"), ("!active", "white")],
        )

        column = tuple(self.headers.keys())

        self.table = ttk.Treeview(
            self.container,
            style="Custom.Treeview",
            columns=column,
            show="headings",
            height=35,
        )

        for key, value in self.headers.items():
            self.table.heading(key, text=value)
            self.table.column(key, anchor="center")

        self.table.pack(expand=ctk.YES, fill=ctk.BOTH)

        if self.data:
            for i in range(len(self.data)):
                values = tuple(self.data[i].get(key) for key in self.headers.keys())
                self.table.insert(
                    parent="",
                    index=0,
                    values=values,
                )
                self.table.bind("<Button-1>", self.on_row_click)

    def on_row_click(self, event):
        item = self.table.identify_row(event.y)
        if item:
            values = self.table.item(item, "values")
            if values:
                id = values[0]
                data = self.function_find.find_by_id(id)
                self.modal = WindowComponent(
                    self.options,
                    self.update_controller,
                    "Actualizar",
                    "update",
                    data,
                    self.remove_controller,
                    width=self.width,
                    height=self.height,
                )
                self.modal.grab_set()
                self.modal.protocol("WM_DELETE_WINDOW", self.__close_modal)

    def __close_modal(self):
        self.modal.grab_release()
        self.modal.destroy()
