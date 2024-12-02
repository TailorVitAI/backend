import os
from enum import Enum
from jinja2 import Template


class CVTemplate(str, Enum):
    TEMPLATE_00 = "template_00.tex"


def generate(cv_template: CVTemplate, data: dict) -> str:
    template_path = os.path.join(
        "apps",
        "main",
        "services",
        "latex",
        "templates",
        cv_template.value,
    )
    with open(template_path, "r") as template_file:
        template_content = template_file.read()

    template = Template(
        source=template_content,
        block_start_string="[[$",
        block_end_string="$]]",
        variable_start_string="[[",
        variable_end_string="]]",
        comment_start_string="#]]",
        comment_end_string="[[#",
    )
    rendered_content = template.render(data)

    return rendered_content
