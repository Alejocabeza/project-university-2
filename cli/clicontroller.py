import os

controller_create_template = """
from controller.Controller import Controller
from models.{model}Model import {model}Model

class {name}Controller(Controller):
    def __init__(self):
        super().__init__()
        self.{model_lower}_repository = {model}Model()

    def create(self, data):
        try:
            data['created_at'] = self._current_time()
            self.{model_lower}_repository.create(data)
        except Exception as ex:
            print(f"Error new {model_lower}: {{ex}}")
            return None
"""

controller_update_template = """
from controller.Controller import Controller
from models.{model}Model import {model}Model

class {name}Controller(Controller):
    def __init__(self):
        super().__init__()
        self.{model_lower}_repository = {model}Model()

    def create(self, id, data):
        try:
            data['updated_at'] = self._current_time()
            self.{model_lower}_repository.update(id, data)
        except Exception as ex:
            print(f"Error update {name}: {{ex}}")
            return None
"""

controller_remove_template = """
from controller.Controller import Controller
from models.{model}Model import {model}Model

class {name}Controller(Controller):
    def __init__(self):
        super().__init__()
        self.{model_lower}_repository = {model}Model()

    def create(self, id):
        try:
            self.{model_lower}_repository.update(id, {'deleted_at': self._current_time()})
        except Exception as ex:
            print(f"Error remove {name}: {{ex}}")
            return None
"""

controller_find_all_template = """
from controller.Controller import Controller
from models.{model}Model import {model}Model

class {name}Controller(Controller):
    def __init__(self):
        super().__init__()
        self.{model_lower}_repository = {model}Model()

    def find_all(self):
        try:
            self.{model_lower}_repository.find_all()
        except Exception as ex:
            print(f"Error finder all {name}: {{ex}}")
            return None
"""

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


def create_controller(name, path, model, type="default"):
    controller_name = name
    controller_content = None
    match type:
        case "create":
            controller_content = controller_create_template.format(
                name=controller_name,
                name_lower=name.lower(),
                model=model,
                model_lower=model.lower(),
            )
        case "update":
            controller_content = controller_update_template.format(
                name=controller_name,
                name_lower=name.lower(),
                model=model,
                model_lower=model.lower(),
            )
        case "remove":
            controller_content = controller_update_template.format(
                name=controller_name,
                name_lower=name.lower(),
                model=model,
                model_lower=model.lower(),
            )
        case "find_all":
            controller_content = controller_find_all_template.format(
                name=controller_name,
                name_lower=name.lower(),
                model=model,
                model_lower=model.lower(),
            )
        case "default":
            controller_content = controller_template.format(
                name=controller_name,
                name_lower=name.lower(),
                model=model,
                model_lower=model.lower(),
            )
    controller_path = os.path.join(path, f"{controller_name}Controller.py")
    create_file(controller_content, controller_path)
