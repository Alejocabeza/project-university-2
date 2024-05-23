import tkinter as tk
from tkinter import font
from Repository.UserRepository import User

class Register(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.userService = User()
        self.create_widget()

    def create_widget(self):
        # Frame
        self.container = tk.LabelFrame(self, text="Register")
        self.container.pack(fill="both", expand=True, pady=150, padx=350)

        #Username
        self.LabelUsername = tk.Label(self.container, text="Username", justify="left", anchor='w')
        self.LabelUsername.pack(fill="both", padx=50, pady=5)
        self.inputUsername = tk.Entry(self.container, name="username")
        self.inputUsername.pack(fill="both", padx=50, pady=0)

        #Email
        self.LabelEmail = tk.Label(self.container, text="Email", justify="left", anchor='w')
        self.LabelEmail.pack(fill="both", padx=50, pady=5)
        self.inputEmail = tk.Entry(self.container, name="email")
        self.inputEmail.pack(fill="both", padx=50, pady=0)

        # Password
        self.LabelPass = tk.Label(self.container, text="Password", justify="left", anchor='w')
        self.LabelPass.pack(fill="both", padx=50, pady=5)
        self.inputPass = tk.Entry(self.container, name="password", show="*")
        self.inputPass.pack(fill="both", padx=50, pady=0)

        # DNI 
        self.LabelDNI = tk.Label(self.container, text="DNI", justify="left", anchor='w')
        self.LabelDNI.pack(fill="both", padx=50, pady=5)
        self.inputDNI = tk.Entry(self.container, name="dni")
        self.inputDNI.pack(fill="both", padx=50, pady=0)

        self.btnSubmit = tk.Button(
            self.container,
            text="Login",
            command=lambda: self.__handleSubmit())
        self.btnSubmit.pack(fill="both", padx=50, pady=20)


    def __handleSubmit(self):
        data_to_insert = {
            "username": self.inputUsername.get(),
            "email": self.inputEmail.get(),
            "password": self.inputPass.get(),
            "dni": self.inputDNI.get()
        }
        result = self.userService.register(data=data_to_insert)
        if(result is False):
            print("Register failed")
        print(result)

