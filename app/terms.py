def run(web):
  # TODO: extract this in fuqit
  path = "/".join(web.path.split("/")[2:])
  return "terms... "+path