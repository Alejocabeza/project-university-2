import customtkinter as ctk

from sections.TableModule import TableModule
from sections.HeaderModule import HeaderModule
from controller.Address.GetAllAddressController import GetAllAddressController
from controller.Address.FindAddressByIdController import FindAddressByIdController
from controller.ClientOffice.CreateClientOfficeController import CreateClientOfficeController
from controller.ClientOffice.GetAllClientOfficeController import GetAllClientOfficeController
from controller.ClientOffice.RemoveClientOfficeController import RemoveClientOfficeController
from controller.ClientOffice.UpdateClientOfficeController import UpdateClientOfficeController
from controller.ClientOffice.FindClientOfficeByIdController import FindClientOfficeByIdController


class ClientOffice(ctk.CTkFrame):
    """
    Vista de ClientOffice
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_client_office_controller = CreateClientOfficeController()
        self.update_client_office_controller = UpdateClientOfficeController()
        self.remove_client_office_controller = RemoveClientOfficeController()
        self.get_all_client_office_controller = GetAllClientOfficeController()
        self.get_all_address_controller = GetAllAddressController()
        self.find_address_by_id = FindAddressByIdController()
        self.find_client_office_by_id = FindClientOfficeByIdController()
        self.window_modal = None
        self.options = [
            {"name": "name", "label": "Nombre", "type": "entry"},
            {"name": "email", "label": "Email", "type": "entry"},
            {"name": "phone", "label": "Telefono", "type": "entry"},
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
        """
        Crea los elementos de la vista
        """
        self.screen = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.screen.pack(expand=ctk.YES, fill=ctk.BOTH)

    def widget_header(self):
        """
        Crea los elementos del encabezado
        """
        HeaderModule(
            self.screen,
            "Sucursales",
            self.refresh,
            self.options,
            self.create_client_office_controller,
        )

    def widget_body(self):
        """
        Crea los elementos del cuerpo principal
        """
        data = self.get_all_client_office_controller.find_all()
        TableModule(
            parent=self.screen,
            headers={
                "id": "ID",
                "name": "Nombre",
                "email": "Email",
                "phone": "Teléfono",
                "address": "Dirección",
            },
            data=data,
            function_find=self.find_client_office_by_id,
            options=self.options,
            update_controller=self.update_client_office_controller,
            remove_controller=self.remove_client_office_controller,
            height=500,
        )

    def refresh(self):
        """
        Refresca la tabla
        """
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

    def __get_name_address(self, id):
        address = self.find_address_by_id.find_by_id(id)
        return address.get("name")
