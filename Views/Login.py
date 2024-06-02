import tkinter as tk
from Repository.UserRepository import User
from config import BLUE, WHITE 

# This class is used as the main window
class Login(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.user = User()
        self.create_widgets()

    def create_widgets(self):
        # Box
        self.formBox = tk.Frame(self, bg=WHITE, bd=0)
        self.formBox.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
        self.imgBox = tk.Frame(self, bg=BLUE, bd=0)
        self.imgBox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.YES)

        # Email
        self.LabelEmail = tk.Label(self.formBox, text="Email", justify="left", anchor='w', width=5)
        self.LabelEmail.pack(fill="both", padx=50, pady=1)
        self.inputEmail = tk.Entry(self.formBox, name="email", border=1, width=5)
        self.inputEmail.pack(fill="both", padx=50, pady=0)       # Email

    def _handleSubmit(self, email, password, confirmedPassword):
        result = self.user.login(email, password, confirmedPassword)
        if(result is None):
            print("Login failed")
        print(result)
