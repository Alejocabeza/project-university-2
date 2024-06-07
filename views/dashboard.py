import customtkinter as ctk


class Dashboard (ctk.CTkFrame):
    """
    Frame para el Dashboard
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        """
        Crea los elementos de la interfaz
        """
        # screen
        self.screen = ctk.CTkFrame(self)
        self.screen.pack(fill=ctk.BOTH, expand=ctk.YES)
