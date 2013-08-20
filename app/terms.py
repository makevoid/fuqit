from jinja2 import Template
from terms_list import terms

def run(web):
  # TODO: extract these in fuqit
  title_url = "/".join(web.path.split("/")[2:])

  term = {}
  for term2 in terms:
    if term2["title_url"] == title_url:
      term = term2

  vars = { "term": term }
  template = web['app'].env.get_template('term.html')

  content = template.render(vars)

  return content