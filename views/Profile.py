import re
import customtkinter as ctk

from config import (
    COLOR_THREE,
    COLOR_FOR,
    COLOR_RED_PRIMARY,
    COLOR_RED_SECONDARY,
    COLOR_BLUE_PRIMARY,
    COLOR_BLUE_SECONDARY,
)
from controller.User.GetUserController import GetUserController
from controller.Auth.AuthUpdateController import AuthUpdateController
from controller.Auth.AuthNewPasswordController import AuthNewPasswordController
from controller.Auth.AuthRemoveAccountController import AuthRemoveAccountController


class Profile(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.auth_update_controller = AuthUpdateController()
        self.auth_get_data_controller = GetUserController()
        self.auth_new_password_controller = AuthNewPasswordController()
        self.auth_remove_account_controller = AuthRemoveAccountController()
        self.show_errors = False
        self.error_type = None
        self.widget_principal_config()
        self.widget_profile_update()
        self.widget_password_update()
        self.widget_remove_user()

    def widget_principal_config(self):
        """
        Crea los elementos del cuerpo principal
        """
        self.widget_body_profile = ctk.CTkScrollableFrame(
            self.parent, fg_color="transparent"
        )
        self.widget_body_profile.pack(fill=ctk.BOTH, expand=ctk.YES)

    def widget_profile_update(self):
        """
        Permite actualizar los datos del usuario
        """

        # Boxes
        self.box_primary = ctk.CTkFrame(
            self.widget_body_profile, fg_color=COLOR_THREE, border_color=COLOR_FOR
        )
        self.box_primary.pack(
            side=ctk.TOP, fill=ctk.BOTH, expand=ctk.YES, padx=5, pady=5
        )

        # Titulo
        self.title = ctk.CTkLabel(
            self.box_primary,
            text="Perfil de Usuario",
            text_color="black",
            font=("Roboto", 30),
            anchor="w",
        )
        self.title.pack(side=ctk.TOP, fill=ctk.BOTH, pady=10, padx=10)

        # Text
        self.title = ctk.CTkLabel(
            self.box_primary,
            text="Actualiza tus datos de perfil",
            text_color="black",
            font=("Roboto", 12),
            anchor="w",
        )
        self.title.pack(side=ctk.TOP, fill=ctk.BOTH, pady=2, padx=10)

        # Container Forms
        self.box_container_input = ctk.CTkFrame(
            self.box_primary, fg_color="transparent"
        )
        self.box_container_input.pack(
            side=ctk.TOP, fill=ctk.BOTH, expand=ctk.YES, padx=10, pady=10
        )

        # Input Name
        self.label = ctk.CTkLabel(
            self.box_container_input,
            text="Nombre",
            text_color="black",
            font=("Roboto", 14),
            anchor="w",
        )
        self.label.pack(side=ctk.TOP, fill=ctk.BOTH, pady=5)
        self.inputName = ctk.CTkEntry(
            self.box_container_input,
            placeholder_text=self.__set_placeholder("name"),
            text_color="black",
            width=250,
            fg_color="transparent",
            height=40,
        )
        self.inputName.pack(side=ctk.TOP, fill=ctk.X)

        # Input Email
        self.label = ctk.CTkLabel(
            self.box_container_input,
            text="Email",
            text_color="black",
            font=("Roboto", 14),
            anchor="w",
        )

        self.label.pack(side=ctk.TOP, fill=ctk.BOTH, pady=5)
        self.inputEmail = ctk.CTkEntry(
            self.box_container_input,
            width=250,
            text_color="black",
            placeholder_text=self.__set_placeholder("email"),
            fg_color="transparent",
            height=40,
        )
        self.inputEmail.pack(side=ctk.TOP, fill=ctk.X)

        # Validation Email if self.show_errors and self.error_type == "email": self.show_validation_errors(self.inputEmail)

        # Input DNI
        self.label = ctk.CTkLabel(
            self.box_container_input,
            text="Cédula",
            text_color="black",
            font=("Roboto", 14),
            anchor="w",
        )
        self.label.pack(side=ctk.TOP, fill=ctk.BOTH, pady=5)
        self.inputDNI = ctk.CTkEntry(
            self.box_container_input,
            placeholder_text=self.__set_placeholder("dni"),
            text_color="black",
            width=250,
            fg_color="transparent",
            height=40,
        )
        self.inputDNI.pack(side=ctk.TOP, fill=ctk.X)

        self.btn_submit = ctk.CTkButton(
            self.box_container_input,
            text="Actualizar",
            font=("Roboto", 14),
            fg_color=COLOR_BLUE_PRIMARY,
            hover_color=COLOR_BLUE_SECONDARY,
            width=250,
            height=40,
            command=lambda: self.__handle_submit("update"),
        )
        self.btn_submit.pack(side=ctk.TOP, fill=ctk.BOTH, pady=20)

    def widget_password_update(self):
        """
        Permite actualizar el password del usuario
        """
        # Boxes
        self.box_primary = ctk.CTkFrame(
            self.widget_body_profile, fg_color=COLOR_THREE, border_color=COLOR_FOR
        )
        self.box_primary.pack(
            side=ctk.TOP, fill=ctk.BOTH, expand=ctk.YES, padx=5, pady=5
        )

        # Titulo
        self.title = ctk.CTkLabel(
            self.box_primary,
            text="Contraseña",
            font=("Roboto", 30),
            text_color="black",
            anchor="w",
        )
        self.title.pack(side=ctk.TOP, fill=ctk.BOTH, pady=10, padx=10)
        # Text
        self.title = ctk.CTkLabel(
            self.box_primary,
            text="Actualiza tu contraseña",
            font=("Roboto", 12),
            text_color="black",
            anchor="w",
        )
        self.title.pack(side=ctk.TOP, fill=ctk.BOTH, pady=2, padx=10)

        # Input Password
        self.box_container_input = ctk.CTkFrame(
            self.box_primary, fg_color="transparent"
        )
        self.box_container_input.pack(
            side=ctk.TOP, fill=ctk.BOTH, expand=ctk.YES, padx=10, pady=10
        )

        self.label = ctk.CTkLabel(
            self.box_container_input,
            text="Contraseña",
            font=("Roboto", 14),
            text_color="black",
            anchor="w",
        )
        self.label.pack(side=ctk.TOP, fill=ctk.BOTH, pady=5)
        self.input_password = ctk.CTkEntry(
            self.box_container_input,
            placeholder_text="Escribe tu contraseña...",
            show="*",
            text_color="black",
            width=250,
            fg_color="transparent",
            height=40,
        )
        self.input_password.pack(side=ctk.TOP, fill=ctk.X)

        if self.show_errors and self.error_type == "password":
            self.show_validation_errors(self.input_password)

        # Input Confirmed Password
        self.label = ctk.CTkLabel(
            self.box_container_input,
            text="Confirma tu contraseña",
            text_color="black",
            font=("Roboto", 14),
            anchor="w",
        )
        self.label.pack(side=ctk.TOP, fill=ctk.BOTH, pady=5)
        self.input_confirmed_password = ctk.CTkEntry(
            self.box_container_input,
            placeholder_text="Escribe tu confirma tu contraseña...",
            text_color="black",
            show="*",
            width=250,
            fg_color="transparent",
            height=40,
        )
        self.input_confirmed_password.pack(side=ctk.TOP, fill=ctk.X)

        if self.show_errors and self.error_type == "confirmed_password":
            self.show_validation_errors(self.input_password)

        self.btn_submit = ctk.CTkButton(
            self.box_container_input,
            text="Actualizar",
            font=("Roboto", 14),
            fg_color=COLOR_BLUE_PRIMARY,
            hover_color=COLOR_BLUE_SECONDARY,
            width=250,
            height=40,
            command=lambda: self.__handle_submit("password"),
        )
        self.btn_submit.pack(side=ctk.TOP, fill=ctk.BOTH, pady=20)

    def widget_remove_user(self):
        """
        Permite borrar el usuario
        """
        # Boxes
        self.box_primary = ctk.CTkFrame(
            self.widget_body_profile, fg_color=COLOR_THREE, border_color=COLOR_FOR
        )
        self.box_primary.pack(
            side=ctk.TOP, fill=ctk.BOTH, expand=ctk.YES, padx=5, pady=5
        )

        # Titulo
        self.title = ctk.CTkLabel(
            self.box_primary,
            text="Eliminar Cuenta",
            text_color="black",
            font=("Roboto", 30),
            anchor="w",
        )
        self.title.pack(side=ctk.TOP, fill=ctk.BOTH, pady=10, padx=10)

        # Text
        self.title = ctk.CTkLabel(
            self.box_primary,
            text="Este proceso no se puede deshacer, es permanente y no se puede recuperar",
            text_color="black",
            font=("Roboto", 12),
            anchor="w",
        )
        self.title.pack(side=ctk.TOP, fill=ctk.BOTH, pady=2, padx=10)

        # Input Name
        self.box_container_input = ctk.CTkFrame(
            self.box_primary, fg_color="transparent"
        )
        self.box_container_input.pack(
            side=ctk.TOP, fill=ctk.BOTH, expand=ctk.YES, padx=10, pady=10
        )

        self.btn_submit = ctk.CTkButton(
            self.box_container_input,
            text="Eliminar Cuenta",
            font=("Roboto", 14),
            fg_color=COLOR_RED_PRIMARY,
            hover_color=COLOR_RED_SECONDARY,
            width=250,
            height=40,
            command=lambda: self.__delete_account(),
        )
        self.btn_submit.pack(side=ctk.TOP, fill=ctk.BOTH, pady=20)

    def show_validation_errors(self, input):
        input.configure(border_color="red")

    def __delete_account(self):
        self.auth_remove_account_controller.remove_account()

    def __set_placeholder(self, field):
        match field:
            case "name":
                return self.auth_get_data_controller.get_user_data().get("name")
            case "email":
                return self.auth_get_data_controller.get_user_data().get("email")
            case "dni":
                if self.auth_get_data_controller.get_user_data().get("dni"):
                    return self.auth_get_data_controller.get_user_data().get("dni")
                else:
                    return "Escribe tu cédula..."

    def __handle_submit(self, type):
        match type:
            case "update":
                data_to_update = {}
                email = self.inputEmail.get()
                name = self.inputName.get()
                dni = self.inputDNI.get()
                if email:
                    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
                    if not re.match(email_pattern, email):
                        self.show_errors = True
                        self.error_type = "email"
                    else:
                        self.show_errors = False
                        self.error_type = None
                        data_to_update["email"] = email
                if name:
                    data_to_update["name"] = name
                if dni:
                    data_to_update["dni"] = dni
                self.auth_update_controller.update(data=data_to_update)
                self.__clear_widgets(self.widget_body_profile)
                self.__render_data()
            case "password":
                data_to_update = {}
                password = self.input_password.get()
                confirmed_password = self.input_confirmed_password.get()
                if password:
                    password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
                    if not re.match(password_pattern, password):
                        self.show_errors = True
                        self.error_type = "password"
                    else:
                        data_to_update["password"] = password
                        self.show_errors = False
                        self.error_type = None
                if confirmed_password:
                    if password != confirmed_password:
                        self.show_errors = True
                        self.error_type = "confirmed_password"
                    else:
                        data_to_update["confirmedPassword"] = confirmed_password
                        self.error_type = None
                        self.show_errors = False
                self.auth_new_password_controller.new_password(data=data_to_update)
                self.__clear_widgets(self.widget_body_profile)
                self.__render_data()

    def __clear_widgets(self, widget):
        for widget in widget.winfo_children():
            widget.destroy()

    def __render_data(self):
        self.widget_profile_update()
        self.widget_password_update()
        self.widget_remove_user()
