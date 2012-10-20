#! /usr/bin/python
#  Name: Sravan Bhamidipati
#  Date: 19th October, 2012
#  Purpose: Main entry point of Twitter Dedupe, a GAE app.


try:
	import jinja2, logging
	from webapp2 import Route, WSGIApplication
	import sys
	if 'lib' not in sys.path:
		sys.path[0:0] = ['lib']
except ImportError:
	print "This application needs the following GAE modules: jinja2, logging, webapp2"
	print "This application needs the following external modules: sys"

routes = [
	Route('/', handler='pages.Home', name='home'),
	Route('/login', handler='pages.Login', name='login'),
	Route('/logout', handler='pages.Logout', name='logout')
]

app = WSGIApplication(routes, debug=True)