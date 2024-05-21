import tkinter as tk
from tkinter import font
from services.User import User

class Register(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.userService = User()
        self.create_widget()

    def create_widget(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Frame
        self.frameForm = tk.LabelFrame(self, text="Register")
        self.frameForm.grid(row=0, column=0, padx=10, pady=10)

        # Username
        self.LabelUsername = tk.Label(self.frameForm, text="Username:", justify="left", anchor='w')
        self.LabelUsername.grid(row=0, column=0, padx=5, pady=5)
        self.InputUsername = tk.Entry(self.frameForm, name="username")
        self.InputUsername.grid(row=0, column=1, padx=5, pady=0)

        # Email
        self.LabelEmail = tk.Label(self.frameForm, text="Email:", justify="left", anchor='w')
        self.LabelEmail.grid(row=0, column=2, padx=5, pady=5)
        self.InputEmail = tk.Entry(self.frameForm, name="email")
        self.InputEmail.grid(row=0, column=3, padx=5, pady=0)

        # Password
        self.LabelPass = tk.Label(self.frameForm, text="Password:", justify="left", anchor='w')
        self.LabelPass.grid(row=1, column=0, padx=5, pady=5)
        self.InputPass = tk.Entry(self.frameForm, name="password", show="*")
        self.InputPass.grid(row=1, column=1, padx=5, pady=0)

        # DNI
        self.labelDNI = tk.Label(self.frameForm, text="DNI:", justify="left", anchor='w')
        self.labelDNI.grid(row=1, column=2, padx=5, pady=5)
        self.inputDNI = tk.Entry(self.frameForm, name="dni")
        self.inputDNI.grid(row=1, column=3, padx=5, pady=5)

        self.data_to_insert={
            "name": self.InputUsername.get(),
            "email": self.InputEmail.get(),
            "password": self.InputPass.get(),
            "DNI": self.inputDNI.get()
        }

        #submit
        self.btnSubmit = tk.Button(
            self.frameForm,
            text="Register",
            command=lambda: self._handleSubmit(self.data_to_insert))
        self.btnSubmit.grid(row=2, column=1, padx=5, pady=5, columnspan=4)

    def _handleSubmit(self, data):
        print(data)
        # result = self.userService.register(email, password, confirmedPassword)
        # if(result is None):
        #     print("Register failed")
        # print(result)

