import os
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

template_dir = os.path.expanduser(
    "~/Workspace/project-university-2/templates/pdf/reports"
)


def create_pdf(template_name, data, name_file):
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(f"{template_name}.html")
    html = template.render(data)
    output_file = os.path.expanduser(
        f"~/Workspace/project-university-2/public/pdf/{name_file}.pdf"
    )
    HTML(string=html).write_pdf(output_file)
    return output_file