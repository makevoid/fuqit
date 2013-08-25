from jinja2 import Template
from db import collection_name

def run(web):
  # rename collection_name with your collection model names (like "posts")
  vars = { "collection_name": collection_name }
  template = web['app'].env.get_template('collection_name.html')
  content = template.render(vars)
  return content