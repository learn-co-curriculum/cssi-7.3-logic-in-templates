import jinja2
import os
import webapp2

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class HelloHandler(webapp2.RequestHandler):
  def get(self):
    names = ['Bart', 'Mushu', 'Stan' , 'Meg']
    template = jinja_environment.get_template('templates/hello.html')
    self.response.out.write(template.render({'names' : names, 'img' : self.request.get('img')}))

routes = [  #a list of tuples mapping paths to handlers

    ('/.*', HelloHandler),
]

app = webapp2.WSGIApplication(routes, debug=True)
