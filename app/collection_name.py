from jinja2 import Template
from db import collection_name

def run(web):
  # TODO: extract these in fuqit
  id = "/".join(web.path.split("/")[2:])

  model = {}
  for mod in collection_name:
    if mod["id"] == id:
      term = mod

  vars = { "term": term }
  template = web['app'].env.get_template('term.html')

  content = template.render(vars)

  return content