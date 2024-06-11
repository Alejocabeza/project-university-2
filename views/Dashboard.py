import customtkinter as ctk


class Dashboard(ctk.CTk):
    def __init__(self, parent):
        self.parent = parent
        self.widgets()

    def widgets(self):
        self.screen = ctk.CTkScrollableFrame(self.parent, fg_color="transparent")
        self.screen.pack(fill=ctk.BOTH, expand=ctk.YES)


