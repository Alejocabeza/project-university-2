import tkinter as tk
from tkinter import font
import utils.util_window as util_window
from config import COLOR_MENU_BACKGROUND, COLOR_SIDEBAR_BACKGROUND, COLOR_BODY_MAIN, COLOR_MENU_CURSOR

# This class is used as the main window
class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config_window()
        self.panels()
        self.controls()

    def config_window(self):
        self.title("Grupo Imnova - Código Fonte")
        w, h = 1024, 600
        util_window.window_center(self, w, h)

    def panels(self):
        # Menu
        self.menu = tk.Frame(self, bg=COLOR_MENU_BACKGROUND, height=50)
        self.menu.pack(side=tk.TOP, fill='both')
        # Sidebar
        self.sidebar = tk.Frame(self, bg=COLOR_SIDEBAR_BACKGROUND, width=200)
        self.sidebar.pack(side=tk.LEFT, fill='both', expand=False)
        # Body
        self.body = tk.Frame(self, bg=COLOR_BODY_MAIN, width=150)
        self.body.pack(side=tk.RIGHT, fill='both', expand=True)

    def controls(self):
        font_awesome = font.Font(family='FontAwesome', size=16)
        # Menu
        self.title = tk.Label(self.menu, text="Grupo Imnova")
        self.title.config(fg="#fff", font=('Roboto', 12), bg=COLOR_MENU_BACKGROUND, pady=10, width=16)
        self.title.pack(side=tk.LEFT)
        # Button Menu
        self.btnMenu = tk.Button(self.menu, text="\uf0c9", font=font_awesome, bd=0, bg=COLOR_MENU_BACKGROUND, fg='white')
        self.btnMenu.pack(side=tk.RIGHT)