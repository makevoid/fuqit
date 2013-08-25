from jinja2 import Template
from db import collection

def run(web):
  # rename collection with your collection model names (like "posts")
  vars = { "collection": collection }
  template = web['app'].env.get_template('collection.html')
  content = template.render(vars)
  return content