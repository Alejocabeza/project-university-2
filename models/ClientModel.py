from models.BaseModel import BaseModel

class ClientModel(BaseModel):
    def __init__(self):
        super().__init__("clients")


    def new_client(self, data):

