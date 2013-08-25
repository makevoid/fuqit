from jinja2 import Template
from db import collection

def run(web):
  # TODO: extract these in fuqit
  id = "/".join(web.path.split("/")[2:])
  model = {}
  for mod in collection:
    if mod["id"] == int(id):
      model = mod

  vars = { "model": model }
  template = web['app'].env.get_template('model.html')

  content = template.render(vars)

  return content