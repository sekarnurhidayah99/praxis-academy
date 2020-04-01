from jinja2 import Template

tmpl = Template(
    """
        <h1>Hallo, {{nama}}</h1>
    """
)

print(tmpl.render(nama='hamurabi'))
