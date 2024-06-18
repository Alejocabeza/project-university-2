import click
from cli.clicontroller import create_controller
from cli.climodel import create_model
from cli.cliviews import create_view


@click.command()
@click.option("--type", prompt="Type", default="resource", help="options: view, controller, model")
def command(type):
    match type:
        case "view":
            name = input("Name of the View: ")
            create_view(name)
        case "controller":
            name = input("Name of the Controller: ")
            path = input("Path of the Controller (default: 'controller'): ") or "controller"
            model = input("Model of the Controller: ")
            create_controller(name, path, model)
        case "model":
            name = input("Name of the Model: ")
            create_model(name)
        case _:
            name = input("Name of the Resource: ")
            path = input("Path of the Controller(default: 'controller'): ") or "controller"
            controllers = ["Create", "GetAll", "Remove", "Update"]
            create_model(name)
            click.echo("Modelo Creado")
            for controller in controllers:
                controller_name = f"{controller}{name.capitalize()}"
                create_controller(name=controller_name, path=path, model=name.capitalize())
                click.echo(f"Controlador {controller_name} Creado")
            create_view(name)
            click.echo("Vista Creada")

if __name__ == "__main__":
    command()
