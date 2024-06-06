import customtkinter as ctk
from views.login import Login
from views.register import Register
from views.dashboard import Dashboard
from lib import util_window


class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Proyecto Universidad Trayecto 2")
        w, h = 1024, 600
        util_window.window_center(self, w, h)
        self.frames = {}
        container = ctk.CTkFrame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for F in (Login, Register, Dashboard):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Login")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = Main()
    app.mainloop()
