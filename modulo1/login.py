import os
import urllib
import jinja2
import webapp2
from webapp2_extras.routes import DomainRoute

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
        def get(self):
                self.response.headers['Content-Type'] = 'text/plain'
                self.response.write('aqui iria el login del modulo 1')

application = webapp2.WSGIApplication([
        DomainRoute('login.mydominio.com', [
                webapp2.Route('/', handler=MainPage, name='login-landing'),                
            ]),
         webapp2.Route('/', MainPage),        
], debug=True)
