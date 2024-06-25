import fontawesome as fa
import customtkinter as ctk

from sections.HeaderModule import HeaderModule
from controller.Address.CreateAddressController import CreateAddressController
from controller.Address.UpdateAddressController import UpdateAddressController
from controller.Address.RemoveAddressController import RemoveAddressController
from controller.Address.GetAllAddressController import GetAllAddressController
from controller.Address.FindAddressByIdController import FindAddressByIdController
from controller.User.FindUserController import FindUserController
from sections.TableModule import TableModule


class Address(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.options = [
            {"name": "name", "label": "Nombre", "type": "entry"},
            {"name": "city", "label": "Ciudad", "type": "entry"},
            {"name": "country", "label": "País", "type": "entry"},
            {"name": "state", "label": "Estado", "type": "entry"},
            {"name": "street", "label": "Calle", "type": "entry"},
            {"name": "postal_code", "label": "Código Postal", "type": "entry"},
            {"name": "location", "label": "Municipio/Localidad", "type": "entry"},
            {
                "name": "department",
                "label": "Urbanización/Departamento/Casa",
                "type": "entry",
            },
        ]
        self.create_address_controller = CreateAddressController()
        self.update_address_controller = UpdateAddressController()
        self.remove_address_controller = RemoveAddressController()
        self.get_all_address_controller = GetAllAddressController()
        self.find_user_controller = FindUserController()
        self.find_address_by_id = FindAddressByIdController()
        self.widgets()
        self.widget_header()
        self.widget_body()

    def widgets(self):
        self.screen = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.screen.pack(expand=ctk.YES, fill=ctk.BOTH)

    def widget_header(self):
        HeaderModule(
            self.screen,
            "Direcciones",
            self.refresh,
            self.options,
            self.create_address_controller,
            height=800,
        )

    def widget_body(self):
        data = self.get_all_address_controller.find_all()
        TableModule(
            parent=self.screen,
            headers={
                "id": "ID",
                "name": "Nombre",
                "main_address": "Dirección Principal",
            },
            data=data,
            function_find=self.find_address_by_id,
            options=self.options,
            update_controller=self.update_address_controller,
            remove_controller=self.remove_address_controller,
            height=800,
        )

    def refresh(self):
        self.__clear_widgets(self.screen)
        self.__render_data()

    def __clear_widgets(self, widget):
        for w in widget.winfo_children():
            w.destroy()

    def __render_data(self):
        self.widget_header()
        self.widget_body()
