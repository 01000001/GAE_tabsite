import os
import urllib

import jinja2
import webapp2
from jinja2 import Template

#import controllers
from _controllers import mainpage

#Rout handlers to urls
application = webapp2.WSGIApplication([
    ('/', mainpage.MainPage),
], debug=True)
