# Name: Sravan Bhamidipati
# Date: 17th October, 2012
# Purpose: Twitter Dedupe, a Googe App Engine application.


import simpleauth, twython, webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write('Hello, webapp World!')


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
