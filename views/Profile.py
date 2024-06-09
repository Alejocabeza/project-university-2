import re
import customtkinter as ctk
from controller.Auth.AuthUpdateController import AuthUpdateController
from controller.Auth.AuthRemoveAccountController import AuthRemoveAccountController
from controller.Auth.AuthCloseSessionController import AuthCloseSessionController
from controller.Auth.AuthNewPasswordController import AuthNewPasswordController
from controller.Auth.AuthGetDataController import AuthGetDataController
from config import WHITE, GRAY, BLACK, SLATE700, SLATE800
from lib import navigation


class Profile(ctk.CTkFrame):
    """
    Frame para el Profile
    """

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.opciones_de_navegacion = navigation.NAVIGATION
        self.profile_update_data_controller = AuthUpdateController()
        self.profile_update_password_controller = AuthNewPasswordController()
        self.profile_remove_controller = AuthRemoveAccountController()
        self.session_close_controller = AuthCloseSessionController()
        self.auth_get_data_controller = AuthGetDataController()
        self.show_errors = False
        self.create_widgets()
        self.widget_superior_config()
        self.widget_lateral_config()
        self.widget_principal_config()
        self.widget_profile_update()
        self.widget_password_update()
        self.widget_remove_user()

    def create_widgets(self):
        """
        Crea los elementos de la interfaz
        """
        # Barra Superior
        self.widget_superior = ctk.CTkFrame(
            self, height=50, fg_color=SLATE800, bg_color=SLATE800
        )
        self.widget_superior.pack(side=ctk.TOP, fill=ctk.BOTH, expand=ctk.NO)

        # Barra Lateral
        self.widget_lateral = ctk.CTkFrame(
            self, height=200, fg_color=SLATE800, bg_color=SLATE800
        )
        self.widget_lateral.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=ctk.NO)

        # Cuerpo
        self.widget_principal = ctk.CTkFrame(self, height=200, fg_color=GRAY)
        self.widget_principal.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=ctk.YES)

    def widget_superior_config(self):
        """
        Crea los elementos de la barra superior
        """
        font_awesome = ctk.CTkFont(family="FontAwesome", size=20)

        # Etiqueta Titulo
        self.label_titulo = ctk.CTkLabel(
            self.widget_superior,
            text="Bienvendio a Grupo Imnova!",
            font=("Roboto", 16),
            pady=10,
            padx=10,
            width=16,
        )
        self.label_titulo.pack(side=ctk.LEFT)

        self.btn_cerrar_sesion = ctk.CTkButton(
            self.widget_superior,
            text="  ",
            font=font_awesome,
            fg_color="transparent",
            bg_color="transparent",
            hover_color="red",
            width=40,
            command=lambda: self.__logout(),
        )
        self.btn_cerrar_sesion.pack(side=ctk.RIGHT, padx=10)

        self.btn_profile_config = ctk.CTkButton(
            self.widget_superior,
            text="  ",
            font=font_awesome,
            fg_color=SLATE700,
            bg_color="transparent",
            hover_color="blue",
            width=40,
            command=lambda: self.controller.show_frame("Profile"),
        )
        self.btn_profile_config.pack(side=ctk.RIGHT)

    def widget_lateral_config(self):
        """
        Crea los elementos de la barra lateral
        """
        # Menu
        for i in range(len(self.opciones_de_navegacion)):
            self.btn_menu = ctk.CTkButton(
                self.widget_lateral,
                text=self.opciones_de_navegacion[i],
                font=("Roboto", 16),
                fg_color="transparent",
                bg_color="transparent",
                height=40,
                width=200,
                command=lambda: self.controller.show_frame(
                    self.opciones_de_navegacion[i]
                ),
            )
            self.btn_menu.pack(side=ctk.TOP, fill=ctk.X, pady=10)

    def widget_principal_config(self):
        """
        Crea los elementos del cuerpo principal
        """
        self.widget_principal_profile = ctk.CTkScrollableFrame(
            self.widget_principal, fg_color="transparent"
        )
        self.widget_principal_profile.pack(
            fill=ctk.BOTH, expand=ctk.YES, padx=10, pady=10
        )

    def widget_profile_update(self):
        """
        Permite actualizar los datos del usuario
        """

        # Boxes
        self.box_primary = ctk.CTkFrame(self.widget_principal_profile, fg_color=WHITE)
        self.box_primary.pack(
            side=ctk.TOP, fill=ctk.BOTH, expand=ctk.YES, padx=10, pady=10
        )

        # Titulo
        self.title = ctk.CTkLabel(
            self.box_primary,
            text="Perfil de Usuario",
            font=("Roboto", 30),
            text_color=BLACK,
            anchor="w",
        )
        self.title.pack(side=ctk.TOP, fill=ctk.BOTH, pady=10, padx=10)

        # Text
        self.title = ctk.CTkLabel(
            self.box_primary,
            text="Actualiza tus datos de perfil",
            font=("Roboto", 12),
            text_color=BLACK,
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
            font=("Roboto", 14),
            text_color=BLACK,
            anchor="w",
        )
        self.label.pack(side=ctk.TOP, fill=ctk.BOTH, pady=5)
        self.inputName = ctk.CTkEntry(
            self.box_container_input,
            text_color=BLACK,
            placeholder_text=self.__set_placeholder("name"),
            width=250,
            fg_color="transparent",
            height=40,
        )
        self.inputName.pack(side=ctk.TOP, fill=ctk.X)

        # Input Email
        self.label = ctk.CTkLabel(
            self.box_container_input,
            text="Email",
            font=("Roboto", 14),
            text_color=BLACK,
            anchor="w",
        )

        self.label.pack(side=ctk.TOP, fill=ctk.BOTH, pady=5)
        self.inputEmail = ctk.CTkEntry(
            self.box_container_input,
            width=250,
            placeholder_text=self.__set_placeholder("email"),
            fg_color="transparent",
            text_color=BLACK,
            height=40,
        )
        self.inputEmail.pack(side=ctk.TOP, fill=ctk.X)

        # Validation Email
        print(self.show_errors)
        if self.show_errors:
            self.show_validation_errors("Email: Debe tener un formato valido", self.box_container_input)

        # Input DNI
        self.label = ctk.CTkLabel(
            self.box_container_input,
            text="Cédula",
            font=("Roboto", 14),
            text_color=BLACK,
            anchor="w",
        )
        self.label.pack(side=ctk.TOP, fill=ctk.BOTH, pady=5)
        self.inputDNI = ctk.CTkEntry(
            self.box_container_input,
            text_color=BLACK,
            placeholder_text=self.__set_placeholder("dni"),
            width=250,
            fg_color="transparent",
            height=40,
        )
        self.inputDNI.pack(side=ctk.TOP, fill=ctk.X)

        self.btn_submit = ctk.CTkButton(
            self.box_container_input,
            text="Actualizar",
            font=("Roboto", 14),
            text_color=WHITE,
            fg_color=SLATE800,
            hover_color=SLATE700,
            width=250,
            height=40,
            command=lambda: self.__handle_submit('update'),
        )
        self.btn_submit.pack(side=ctk.TOP, fill=ctk.BOTH, pady=20)

    def widget_password_update(self):
        """
        Permite actualizar el password del usuario
        """
        # Boxes
        self.box_primary = ctk.CTkFrame(self.widget_principal_profile, fg_color=WHITE)
        self.box_primary.pack(
            side=ctk.TOP, fill=ctk.BOTH, expand=ctk.YES, padx=10, pady=10
        )

        # Titulo
        self.title = ctk.CTkLabel(
            self.box_primary,
            text="Contraseña",
            font=("Roboto", 30),
            text_color=BLACK,
            anchor="w",
        )
        self.title.pack(side=ctk.TOP, fill=ctk.BOTH, pady=10, padx=10)
        # Text
        self.title = ctk.CTkLabel(
            self.box_primary,
            text="Actualiza tu contraseña",
            font=("Roboto", 12),
            text_color=BLACK,
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
            text_color=BLACK,
            anchor="w",
        )
        self.label.pack(side=ctk.TOP, fill=ctk.BOTH, pady=5)
        self.input_password = ctk.CTkEntry(
            self.box_container_input,
            placeholder_text="Escribe tu contraseña...",
            width=250,
            fg_color="transparent",
            height=40,
        )
        self.input_password.pack(side=ctk.TOP, fill=ctk.X)

        # Input Confirmed Password
        self.label = ctk.CTkLabel(
            self.box_container_input,
            text="Confirma tu contraseña",
            font=("Roboto", 14),
            text_color=BLACK,
            anchor="w",
        )
        self.label.pack(side=ctk.TOP, fill=ctk.BOTH, pady=5)
        self.input_confirmed_password = ctk.CTkEntry(
            self.box_container_input,
            placeholder_text="Escribe tu confirma tu contraseña...",
            width=250,
            fg_color="transparent",
            height=40,
        )
        self.input_confirmed_password.pack(side=ctk.TOP, fill=ctk.X)

        data_to_update = {}

        if self.input_password.get() is not None:
            data_to_update["password"] = self.input_password.get()
        if self.input_confirmed_password.get() is not None:
            data_to_update["confirmed_password"] = self.input_confirmed_password.get()

        self.btn_submit = ctk.CTkButton(
            self.box_container_input,
            text="Actualizar",
            font=("Roboto", 14),
            text_color=WHITE,
            fg_color=SLATE800,
            hover_color=SLATE700,
            width=250,
            height=40,
            command=lambda: self.profile_update_password_controller.new_password(
                data=data_to_update
            ),
        )
        self.btn_submit.pack(side=ctk.TOP, fill=ctk.BOTH, pady=20)

    def widget_remove_user(self):
        """
        Permite borrar el usuario
        """
        # Boxes
        self.box_primary = ctk.CTkFrame(self.widget_principal_profile, fg_color=WHITE)
        self.box_primary.pack(
            side=ctk.TOP, fill=ctk.BOTH, expand=ctk.YES, padx=10, pady=10
        )

        # Titulo
        self.title = ctk.CTkLabel(
            self.box_primary,
            text="Eliminar Cuenta",
            font=("Roboto", 30),
            text_color=BLACK,
            anchor="w",
        )
        self.title.pack(side=ctk.TOP, fill=ctk.BOTH, pady=10, padx=10)

        # Text
        self.title = ctk.CTkLabel(
            self.box_primary,
            text="Este proceso no se puede deshacer, es permanente y no se puede recuperar",
            font=("Roboto", 12),
            text_color=BLACK,
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
            text_color=WHITE,
            fg_color="red",
            hover_color=SLATE700,
            width=250,
            height=40,
            command=lambda: self.__delete_account(),
        )
        self.btn_submit.pack(side=ctk.TOP, fill=ctk.BOTH, pady=20)

    def show_validation_errors(self, error_text, parent):
        error_label = ctk.CTkLabel(
            parent,
            text=error_text,
            width=500,
            anchor="w",
            fg_color="red",
            corner_radius=5,
        )
        error_label.pack(expand=True, pady=10)

    def __logout(self):
        self.session_close_controller.close_session()
        self.controller.show_frame("Login")

    def __delete_account(self):
        self.profile_remove_controller.remove_account()
        self.controller.show_frame("Login")

    def __set_placeholder(self, field):
        match field:
            case 'name':
                return self.auth_get_data_controller.get_user_data().get('nombre')
            case 'email':
                return self.auth_get_data_controller.get_user_data().get('email')
            case 'dni':
                if self.auth_get_data_controller.get_user_data().get('cedula'):
                    return self.auth_get_data_controller.get_user_data().get('cedula')
                else:
                    return "Escribe tu cédula..."

    def __handle_submit(self, type):
        match type:
            case 'update':
                data_to_update = {}
                email = self.inputEmail.get()
                name = self.inputName.get()
                dni = self.inputDNI.get()
                if email:
                    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
                    if not re.match(email_pattern, email):
                        self.show_errors = True
                    else:
                        data_to_update["email"] = email
                if name:
                    data_to_update["nombre"] = name
                if dni:
                    data_to_update["cedula"] = dni
                self.profile_update_data_controller.update(data=data_to_update)