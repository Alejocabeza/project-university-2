import tkinter as tk
from tkinter import font
import utils.util_window as util_window
from config import COLOR_MENU_BACKGROUND, COLOR_SIDEBAR_BACKGROUND, COLOR_BODY_MAIN, COLOR_MENU_CURSOR
from services.User import User

# This class is used as the main window
class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config_window()
        self.panel()
        self.form()
        self.user = User()

    def config_window(self):
        self.title("Proyecto Universidad Trayecto 2 - Login")
        w, h = 1024, 600
        util_window.window_center(self, w, h)

    def panel(self):
        self.body = tk.Frame(self, bg=COLOR_MENU_BACKGROUND, height=150)
        self.body.pack(fill="both", expand=True)

    def form(self):
        self.frameForm = tk.Frame(self.body, bg=COLOR_BODY_MAIN)
        self.frameForm.pack(fill="both", expand=True, pady=150, padx=350)

        self.LabelForm = tk.Label(self.frameForm, text="Login", font=font.Font(size=30, weight="bold"), bg=COLOR_BODY_MAIN, fg=COLOR_MENU_CURSOR)
        self.LabelForm.pack(fill="x", padx=10, pady=10)

        self.labelEmail = tk.Label(self.frameForm, text="Correo Electrónico", bg=COLOR_BODY_MAIN, fg=COLOR_MENU_CURSOR)
        self.labelEmail.pack(fill="both")
        self.inputEmail = tk.Entry(self.frameForm)
        self.inputEmail.pack(fill="x", padx=50, pady=10)

        self.labelPassword = tk.Label(self.frameForm, text="Contraseña", bg=COLOR_BODY_MAIN, fg=COLOR_MENU_CURSOR)
        self.labelPassword.pack(fill="both")
        self.inputPassword = tk.Entry(self.frameForm, show="*")
        self.inputPassword.pack(fill="x", padx=50, pady=10)

        self.labelConfirmedPassword = tk.Label(self.frameForm, text="Confirma tú contraseña", bg=COLOR_BODY_MAIN, fg=COLOR_MENU_CURSOR)
        self.labelConfirmedPassword.pack(fill="both")
        self.inputConfirmedPassword = tk.Entry(self.frameForm, show="*")
        self.inputConfirmedPassword.pack(fill="x", padx=50, pady=10)

        self.submitButton = tk.Button(self.frameForm, text="Login", command=lambda: handleSubmit(self.inputEmail.get(), self.inputPassword.get(), self.inputConfirmedPassword.get()))
        self.submitButton.pack(fill="x", padx=50, pady=10)

        self.inputRemember = tk.Checkbutton(self.frameForm, text="Remember me")
        self.inputRemember.pack(fill="x", padx=50, pady=10)

        def handleSubmit(email, password, confirmedPassword):
            print(email, password, confirmedPassword)
            result = self.user.login(email, password, confirmedPassword)
            if(result is None):
                print("Login failed")
            print(result)