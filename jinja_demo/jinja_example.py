from jinja2 import Environment, FileSystemLoader

templateLoader = FileSystemLoader(searchpath=r"D:")

templateEnv = Environment(loader=templateLoader)

TEMPLATE_FILE = "sample.html"

template = templateEnv.get_template(TEMPLATE_FILE)

templateVars = {"title": "Test Example",
                "description": "A simple inquiry of function."}

outputText = template.render(templateVars)

print(outputText)
