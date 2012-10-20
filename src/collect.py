#! /usr/bin/python
#  Name: Sravan Bhamidipati
#  Date: 19th October, 2012
#  Purpose: To collect tweets from a user or from my timeline.
#  WARNING: INTERNAL SCRIPT. NO EXCEPTION HANDLING. USE CAREFULLY TO AVOID HITTING RATE LIMITS.

from twython import Twyton
import os, secrets, sys, time

if len(sys.argv) == 3:
	operation = sys.argv[1]
	tweets_file = sys.argv[2]
else:
	print "Usage: python", sys.argv[0], "home|<username> <tweets_file>"
	print '"home" to get tweets seen in my timeline.'
	print '<username> to get a user\'s tweets'
	sys.exit(0)

twitter = Twython(twitter_token=secrets.TWITTER_CONSUMER_KEY, twitter_secret=secrets.TWITTER_CONSUMER_SECRET, oauth_token=secrets.TWITTER_OAUTH_TOKEN, oauth_token_secret=secrets.TWITTER_OAUTH_TOKEN_SECRET)

# Look for authentication and rate-limiting errors.
# twython.TwythonAuthError(), twython.TwythonRateLimitError()

cred_dict = twitter.verifyCredentials()


def user():
	fd = open(tweets_file, 'w')
	for p in range(1,11):
		for tweet in twitter.getUserTimeline(count="100", page=str(p), screen_name=operation):
			fd.write(tweet['text'].encode('utf-8'))
			fd.write('\n')
		time.sleep(10)
	fd.flush()
	fd.close()


def home():
	fd = open(tweets_file, 'w')
	for p in range(1,11):
		for tweet in twitter.getHomeTimeline(count="100", page=str(p)):
			fd.write(tweet['text'].encode('utf-8'))
			fd.write('\n')
		time.sleep(10)
	fd.flush()
	fd.close()


if operation is "home":
	home()
else:
	user()