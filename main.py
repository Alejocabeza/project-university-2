import tkinter as tk
import utils.util_window as util_window

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config_window()

    def config_window(self):
        self.title("Grupo Imnova - Código Fonte")
        w, h = 1024, 600
        util_window.window_center(self, w, h)

app = Main()
app.mainloop()