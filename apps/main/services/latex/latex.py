import os
import logging
import shutil
import subprocess
from enum import Enum
from jinja2 import Template


class CVTemplate(str, Enum):
    TEMPLATE_00 = "temp_00"


def __get_template_path(template: CVTemplate) -> str:
    template_path = os.path.join(
        "apps",
        "main",
        "services",
        "latex",
        "templates",
        template.value,
    )
    return template_path


def generate(cv_template: CVTemplate, data: dict) -> str:
    with open(
        os.path.join(__get_template_path(cv_template), "main.tex"), "r"
    ) as template_file:
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


def compile(template, content, output_dir: str = "./output"):

    filename = "document"
    os.makedirs(output_dir, exist_ok=True)

    tex_file = os.path.join(output_dir, f"{filename}.tex")
    pdf_file = os.path.join(output_dir, f"{filename}.pdf")

    # Copy assets
    source_dir = __get_template_path(template)
    for file_name in os.listdir(source_dir):
        if file_name.endswith(".png"):
            source_file = os.path.join(source_dir, file_name)
            target_file = os.path.join(output_dir, file_name)
            shutil.copy(source_file, target_file)
            logging.debug(f"Copied: {source_file} to {target_file}")

    # Write LaTeX content to file
    with open(tex_file, "w", encoding="utf-8") as f:
        f.write(content)

    compile_cmd = [
        "pdflatex",
        "-shell-escape",
        "-interaction=nonstopmode",
        "-output-directory",
        output_dir,
        tex_file,
    ]
    result = subprocess.run(
        compile_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    logging.error(result.stdout)
    logging.error(result.stderr)

    return pdf_file
