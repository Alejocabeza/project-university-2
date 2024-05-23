import tkinter as tk
from Repository.UserRepository import User

# This class is used as the main window
class Login(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.user = User()
        self.create_widgets()

    def create_widgets(self):
        # Frame
        self.frameForm = tk.LabelFrame(self, text="Login")
        self.frameForm.pack(fill="both", expand=True, pady=150, padx=350)

        # Email
        self.LabelEmail = tk.Label(self.frameForm, text="Email", justify="left", anchor='w')
        self.LabelEmail.pack(fill="both", padx=50, pady=5)
        self.inputEmail = tk.Entry(self.frameForm, name="email")
        self.inputEmail.pack(fill="both", padx=50, pady=0)

        # Password
        self.LabelPass = tk.Label(self.frameForm, text="password", justify="left", anchor='w')
        self.LabelPass.pack(fill="both", padx=50, pady=5)
        self.inputPass = tk.Entry(self.frameForm, name="password", show="*")
        self.inputPass.pack(fill="both", padx=50, pady=0)

        # Confirmed Password
        self.LabelPassConfirmed = tk.Label(self.frameForm, text="Confirmed Password", justify="left", anchor='w')
        self.LabelPassConfirmed.pack(fill="both", padx=50, pady=5)
        self.inputPassConfirmed = tk.Entry(self.frameForm, name="confirmed Password", show="*")
        self.inputPassConfirmed.pack(fill="both", padx=50, pady=0)

        self.btnSubmit = tk.Button(
            self.frameForm,
            text="Login",
            command=lambda: self._handleSubmit(self.inputEmail.get(), self.inputPass.get(), self.inputPassConfirmed.get()))
        self.btnSubmit.pack(fill="both", padx=50, pady=20)

        self.btnRegiser = tk.Button(
            self.frameForm,
            text="Register",
            command=lambda: self.controller.show_frame("Register"))
        self.btnRegiser.pack(fill="both", padx=50, pady=20)

    def _handleSubmit(self, email, password, confirmedPassword):
        print(email, password, confirmedPassword)
        result = self.user.login(email, password, confirmedPassword)
        if(result is None):
            print("Login failed")
        print(result)
