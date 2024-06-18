import os

# Plantilla para el controlador
controller_template = """
from controller.Controller import Controller
from models.{model}Model import {model}Model

class {name}Controller(Controller):
    def __init__(self):
        super().__init__()
        self.{model_lower}_repository = {model}Model()
"""


def create_file(content, path):
    # Crear directorio si no existe
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)


def create_controller(name, path, model):
    controller_name = name
    controller_content = controller_template.format(
        name=controller_name,
        name_lower=name.lower(),
        model=model,
        model_lower=model.lower(),
    )
    controller_path = os.path.join(path, f"{controller_name}Controller.py")
    create_file(controller_content, controller_path)
