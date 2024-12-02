import os

from jinja2 import Template


def render_template(template_name: str, date: dict) -> str:

    template_path = os.path.join(
        "apps", "main", "services", "latex", "templates", template_name
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


if __name__ == "__main__":
    data = {
        "name": "Mahdi Massahi",
        "title": "Machine Learning Engineer (GenAI)",
        "company": "Neuroship B.V.",
        "location": "Den Haag, Netherlands",
        "telephone": "+31xxx",
        "email": "mahdi@neuroship.ai",
        "linkedin": "linkedin",
        "website": "https://brison.dev",
        "github": "https://github.com/mahdi-massahi",
        "summary": "This is a dynamically generated summary for the report.",
        "skills": [
            "a",
            "b",
            "c",
        ],
        "interests": ["x", "y", "z"],
    }

    res = render_template("template_00.tex", data)
    print(res)
