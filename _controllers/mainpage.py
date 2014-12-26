import os
import urllib

import jinja2
import webapp2
from jinja2 import Template

#Initialize Jinja environment
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
#generate major arpeggio
def majorArpeggioGenerator(scale):
		""" input integer, output string
		Takes an integer as input, outputs a string for a major arpeggio run
		that can be parsed by tabvex.
		
		"""
		
		#which scale
		modifier = scale - 1
		
		#xth note of the scale on the nth string
		FirstPerFifth = 3 + modifier
		ThirdPerFourth = 2 + modifier
		FiftPerThird = 0 + modifier
		FirstPerSecond = 1 + modifier
		ThirdPerFirst = 0 + modifier
		FifthPerFirst = 3 + modifier
		ThirdPerSecond = 5 + modifier
		FirstPerThird = 5 + modifier
		FifthPerFourth = 5 + modifier
		ThirdPerFifth = 7 + modifier
		
		allNotes = (FirstPerFifth, ThirdPerFourth, FiftPerThird, FirstPerSecond,
		ThirdPerFirst, FifthPerFirst, ThirdPerSecond, FirstPerThird, FifthPerFourth, ThirdPerFifth)
		
		noteTemplate = "notes %i/5 %i/4 %i/3 %i/2 %i/1 %i/1 %i/2 %i/3 %i/4 %i/5" % allNotes
					
		return noteTemplate
		

#generate notes for rendering tab
def noteGenerator():
		""" input integer, output string
		Generates a string that can be parsed by tabvex.
		Takes an integer as input, 1 indicates the C major scale, 2 C# major and so on.
		"""
		
		needed = majorArpeggioGenerator(1)
		
		noteTemplate = """
					tabstave
					%s |
					notes 3/5 5/5 7/5 3/4 5/4 7/4 4/3
					
					tabstave
					notation=false
					
					notes 5/3 4/3 7/4 5/4 3/4 7/5 5/5 |
					notes 3/5 7/5 5/4 5/3 5/2 3/1 0/1 1/2 0/3 2/4
					
					tabstave
					notation=false
					
					notes 3/5 0/4 2/4 3/4 0/3 2/3 4/3 |
					notes 1/2 4/3 2/3 0/3 3/4 2/4 0/4 3/5""" % needed
		
		return noteTemplate


class MainPage(webapp2.RequestHandler):
    def get(self):
        
        templateValues = {
        		'noteTemplate': noteGenerator(),
        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(templateValues))
