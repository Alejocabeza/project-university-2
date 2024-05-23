import tkinter as tk

class Dashboard(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widget()

    def create_widget(self):
        self.panels()

    def panels(self):
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)