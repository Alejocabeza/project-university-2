import click
from cli.clicontroller import create_controller
from cli.climodel import create_model
from cli.cliviews import create_view


@click.command()
@click.option(
    "--type", prompt="Type", default="resource", help="options: view, controller, model"
)
def command(type):
    match type:
        case "view":
            name = input("Name of the View: ")
            options = []
            while True:
                name = input("Indicame el nombre que va tener esta options: ")
                label = input("Indicame el label que va tener esta options: ")
                type = input("Esta opción es de tipo 'Entry'? (y/n)")
                if type == "n":
                    combobox_option = []
                    while True:
                        request = input("Quieres agregar una opción (y/n)? ")
                        if request == "n":
                            break
                        combobox_option.append(input("Indicame la opción: "))
                    options.append(
                        {
                            "name": name,
                            "label": label,
                            "type": "combobox",
                            "options": combobox_option,
                        }
                    )
                options.append({"name": name, "label": label, "type": "entry"})
                request = input("Quieres agregar una option (y/n)? ")
                if request == "n":
                    break
            create_view(name, options=options)
        case "controller":
            name = input("Name of the Controller: ")
            path = (
                input("Path of the Controller (default: 'controller'): ")
                or "controller"
            )
            model = input("Model of the Controller: ")
            create_controller(name, path, model)
        case "model":
            name = input("Name of the Model: ")
            create_model(name)
        case _:
            name_res = input("Name of the Resource: ")
            path = (
                input("Path of the Controller(default: 'controller'): ") or "controller"
            )
            controllers = ["Create", "GetAll", "Remove", "Update"]
            create_model(name_res)
            click.echo("Modelo Creado")
            for controller in controllers:
                controller_name = f"{controller}{name_res.capitalize()}"
                create_controller(
                    name=controller_name, path=path, model=name_res.capitalize()
                )
                click.echo(f"Controlador {controller_name} Creado")
            options = []
            while True:
                name = input("Indicame el nombre que va tener esta options: ")
                label = input("Indicame el label que va tener esta options: ")
                type = input("Esta opción es de tipo 'Entry'? (y/n)")
                if type == "n":
                    combobox_option = []
                    while True:
                        request = input("Quieres agregar una opción (y/n)? ")
                        if request == "n":
                            break
                        combobox_option.append(input("Indicame la opción: "))
                    options.append(
                        {
                            "name": name,
                            "label": label,
                            "type": "combobox",
                            "options": combobox_option,
                        }
                    )
                options.append({"name": name, "label": label, "type": "entry"})
                request = input("Quieres agregar una option (y/n)? ")
                if request == "n":
                    break
            create_view(name_res, options)
            click.echo("Vista Creada")

if __name__ == "__main__":
    command()
