from models.BaseModel import BaseModel

class ClientModel(BaseModel):
    def __init__(self):
        super().__init__("clientes")


    def new_client(self, data):

