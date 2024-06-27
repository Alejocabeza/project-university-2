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
            name_res = input("Name of the View: ")
            name_spanish = input("Name of the View in Spanish: ")
            options = []
            while True:
                name = input("option name: ")
                label = input("option label: ")
                type = input("This option is of type 'Entry'? (y/n)")
                if type == "n":
                    combobox_option = []
                    while True:
                        request = input("You want to add a option (y/n)? ")
                        if request == "n":
                            break
                        combobox_option.append(input("option combobox: "))
                    options.append(
                        {
                            "name": name,
                            "label": label,
                            "type": "combobox",
                            "options": combobox_option,
                        }
                    )
                options.append({"name": name, "label": label, "type": "entry"})
                request = input("You want to add a new option (y/n)? ")
                if request == "n":
                    break
            create_view(name=name_res, name_spanish=name_spanish, options=options)
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
            name_spanish = input("Name of the Resource in Spanish: ")
            controllers = ["Create", "GetAll", "FindById", "Remove", "Update"]
            create_model(name_res)
            click.echo("Model Created")
            for controller in controllers:
                controller_name = f"{controller}{name_res.capitalize()}"
                match controller:
                    case "Create":
                        create_controller(
                            name=controller_name,
                            path=path,
                            model=name_res.capitalize(),
                            type="create",
                        )
                        click.echo(f"Controller {controller_name} created")
                    case "GetAll":
                        create_controller(
                            name=controller_name,
                            path=path,
                            model=name_res.capitalize(),
                            type="find_all",
                        )
                        click.echo(f"Controller {controller_name} created")
                    case "Remove":
                        create_controller(
                            name=controller_name,
                            path=path,
                            model=name_res.capitalize(),
                            type="remove",
                        )
                        click.echo(f"Controller {controller_name} created")
                    case "Update":
                        create_controller(
                            name=controller_name,
                            path=path,
                            model=name_res.capitalize(),
                            type="update",
                        )
                        click.echo(f"Controller {controller_name} created")
                    case "FindById":
                        create_controller(
                            name=controller_name,
                            path=path,
                            model=name_res.capitalize(),
                            type="find_by_id",
                        )
                        click.echo(f"Controller {controller_name} created")
            options = []
            while True:
                name = input("option name: ")
                label = input("option label: ")
                type = input(
                    "This option is of type (entry, dateentry, combobox, textbox, checkbox)? "
                )
                if type == "combobox":
                    combobox_option = []
                    while True:
                        request = input("You want to add a option on combobox (y/n)? ")
                        if request == "n":
                            options.append(
                                {
                                    "name": name,
                                    "label": label,
                                    "type": "combobox",
                                    "options": combobox_option,
                                }
                            )
                            break
                        combobox_option.append(
                            input("name of the option for combobox: ")
                        )
                        options.append(
                            {
                                "name": name,
                                "label": label,
                                "type": "combobox",
                                "options": combobox_option,
                            }
                        )
                else:
                    options.append({"name": name, "label": label, "type": type})
                request = input("You want to add a new option (y/n)? ")
                if request == "n":
                    break
            create_view(name_res, options, name_spanish)
            click.echo("View Created")


if __name__ == "__main__":
    command()
