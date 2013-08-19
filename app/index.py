from jinja2 import Template
from terms_list import terms
# from jinja.environment import Environment

def run(web):
  vars = { "terms": terms }
  template = web['app'].env.get_template('terms.html')
  content = template.render(vars)
  # env = Environment()
  # # env.loader = FileSystemLoader('app/')
  # tmpl = env.get_template('app/terms.html')
  # content = tmpl.render(vars)

  
  # template = open("app/terms.html").read()
  # template = Template(template)
  # content = template.render(name='John Doe')

  return content


