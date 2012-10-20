#! /usr/bin/python
#  Name: Sravan Bhamidipati
#  Date: 19th October, 2012
#  Purpose: Different pages and page handling for Twitter Dedupe.


try:
	import jinja2, logging
	from webapp2 import RequestHandler
	from twython import Twython
	import secrets
except ImportError:
	print "This application needs the following GAE modules: jinja2, logging, webapp2"
	print "This application needs the following libraries: twython"

jenv = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))

class Home(RequestHandler):
	def get(self):
		template = jenv.get_template("home.html")
		self.response.out.write(template.render())


class Login(RequestHandler):
	def get(self):
		twitter = Twython(twitter_token=secrets.TWITTER_CONSUMER_KEY, twitter_secret=secrets.TWITTER_CONSUMER_SECRET, callback_url="/")
		logging.info("Instantiated Twython object.")
		auth_props = twitter.get_authentication_tokens()
		logging.info(auth_props.auth_url)
		# url = '%s&oauth_callback=%s' % (auth_props.auth_url, callback_url)
		# self.redirect(url)


class Logout(RequestHandler):
	def get(self):
		pass
