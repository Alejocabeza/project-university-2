import customtkinter as ctk

from sections.TableModule import TableModule
from sections.HeaderModule import HeaderModule
from controller.Clients.CreateClientController import CreateClientController
from controller.Clients.GetAllClientController import GetAllClientController
from controller.Clients.RemoveClientController import RemoveClientController
from controller.Clients.UpdateClientController import UpdateClientController
from controller.Address.GetAllAddressController import GetAllAddressController
from controller.Clients.FindClientByIdController import FindClientByIdController
from controller.Address.FindAddressByIdController import FindAddressByIdController
from controller.ClientOffice.GetAllClientOfficeController import GetAllClientOfficeController
from controller.ClientOffice.FindClientOfficeByIdController import FindClientOfficeByIdController


class Clients(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_client_controller = CreateClientController()
        self.update_client_controller = UpdateClientController()
        self.remove_client_controller = RemoveClientController()
        self.get_all_client_controller = GetAllClientController()
        self.get_all_address_controller = GetAllAddressController()
        self.find_address_by_id = FindAddressByIdController()
        self.get_all_client_office_controller = GetAllClientOfficeController()
        self.find_client_office_by_id = FindClientOfficeByIdController()
        self.find_client_by_id = FindClientByIdController()
        self.options = [
            {"name": "name", "label": "Nombre", "type": "entry"},
            {"name": "dni", "label": "DNI/RIF", "type": "entry"},
            {"name": "email", "label": "Email", "type": "entry"},
            {"name": "phone", "label": "Telefono", "type": "entry"},
            {
                "name": "type",
                "label": "Tipo de Cliente",
                "type": "combobox",
                "options": [
                    "Persona Natural",
                    "Persona Jurídica",
                    "Gubernamental",
                ],
            },
            {
                "name": "client_office",
                "label": "Sucursal del Cliente",
                "type": "combobox",
                "options": self.__get_client_office_all(),
            },
            {
                "name": "address",
                "label": "Dirección",
                "type": "combobox",
                "options": self.__get_address_all(),
            },
        ]
        self.widgets()
        self.widget_header()
        self.widget_body()

    def widgets(self):
        self.screen = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.screen.pack(expand=ctk.YES, fill=ctk.BOTH)

    def widget_header(self):
        HeaderModule(
            self.screen,
            "Clientes",
            self.refresh,
            self.options,
            self.create_client_controller,
        )

    def widget_body(self):
        # container
        data = self.get_all_client_controller.find_all()
        TableModule(
            self.screen,
            {
                "id": "ID",
                "name": "Nombre",
                "dni": "DNI/RIF",
                "email": "Email",
                "phone": "Telefono",
                "type": "Tipo de Cliente",
                "address": "Dirección",
                "client_office": "Sucursal del Cliente",
            },
            data,
            self.find_client_by_id,
            self.options,
            self.update_client_controller,
            self.remove_client_controller,
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

    def __get_address_all(self):
        data_to_return = list()
        data = self.get_all_address_controller.find_all()
        if data:
            for address in data:
                data_to_return.append(address.get("name"))
        else:
            data_to_return.append("Sin Dirección")
        return data_to_return

    def __get_client_office_all(self):
        data_to_return = list()
        data = self.get_all_client_office_controller.find_all()
        if data:
            for client_office in data:
                data_to_return.append(client_office.get("name"))
        else:
            data_to_return.append("Sin Sucursal")
        return data_to_return

    def __get_name_address(self, id):
        address = self.find_address_by_id.find_by_id(id)
        if address:
            return address.get("name")
        return "Sin Dirección"

    def __get_name_client_office(self, id):
        client_office = self.find_client_office_by_id.find_by_id(id)
        if client_office:
            return client_office.get("name")
        return "Sin Sucursal"

    def __get_type_client(self, type):
        match type:
            case "person":
                return "Persona Natural"
            case "company":
                return "Persona Jurídica"
            case "government":
                return "Gubernamental"
