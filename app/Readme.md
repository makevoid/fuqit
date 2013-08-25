# TheApp

this is your first fuqit webapp! it's awesome, and you can do dafuq you want! enjoy!


the main example it's a collection taken from a db (that's just an array of dictionaries)


when you find something name "collection_name" it's the name of the collection (for example "posts") and "model" also, has to be replaced with the singular version (e.g. "post")

I added a guardfile for automatic compiling of SASS to CSS

run it with guard:

    guard

if tou don't have it:

    gem install guard guard-sass


---

### some fuqit examples:

other ways to return stuff

    def test(instuff):
      return "OUT %r" % instuff


use urlopen or other net/scraping libraries to have all the web in the palm of your requests! :D example:

    from urllib import urlopen


    def run(web):
      cont = urlopen("http://localhost:3000").readlines()
      return cont


for getting values from a form:

    def run(web):
      headers = [(k,v) for k,v in web.headers.items()]

      result = "HEADERS: %r\nPARAMS: %r\nPATH: %r\nMETHOD: %r" % (
          headers, web.params, web.path, web.method)

      return result, 200, {'content-type': 'text/plain'}


use:

    {% set stuff = module('stuff') %}

in your templates to include helpers