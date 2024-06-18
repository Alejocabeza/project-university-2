import os

# Plantilla para el controlador
model_template = """
from models.BaseModel import BaseModel

class {name}Model(BaseModel):
    def __init__(self):
        super().__init__('{name_lower}')
"""


def create_file(content, path):
    # Crear directorio si no existe
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)


def create_model(name):
    model_name = name.capitalize()
    model_content = model_template.format(
        name=model_name,
        name_lower=name.lower(),
    )
    model_path = os.path.join("models", f"{model_name}Model.py")
    create_file(model_content, model_path)
