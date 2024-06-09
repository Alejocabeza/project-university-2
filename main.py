import customtkinter as ctk
from views.Login import Login
from views.Register import Register
from views.Dashboard import Dashboard
from views.Profile import Profile
from lib import util_window
from config import SLATE700


class Main(ctk.CTk):
    """
    Clase principal del proyecto
    """

    def __init__(self):
        super().__init__()
        self.title("Grupo Imnova")
        w, h = 1024, 600
        util_window.window_center(self, w, h)
        self.frames = {}
        container = ctk.CTkFrame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for F in (Login, Register):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Login")

    def show_frame(self, page_name):
        """
        Muestra el frame correspondiente al nombre de la clase
        """
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = Main()
    app.mainloop()
