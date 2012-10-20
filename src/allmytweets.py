#! /usr/bin/python
#  Name: Sravan Bhamidipati
#  Date: 19th October, 2012
#  Purpose: To parse tweets from www.AllMyTweets.net pages.

import os, re, sys

if len(sys.argv) == 3:
	from_file = sys.argv[1]
	to_file = sys.argv[2]
else:
	print "Usage: python", sys.argv[0], "<from_html_file> <to_tweets_file>"

from_fd = open(from_file, 'r')
to_fd = open(to_file, 'w')
tweets = ""
start = 0

for line in from_fd.readlines():
	if "<ul><li>" in line:
		start = 1
	if start == 1:
		tweets += line.strip()
	if "</div" in line:
		start = 0

from_fd.close()

for tweet in tweets.split("</li><li>"):
	tweet = re.sub("<a href.*>h", "h", tweet.split("<span")[0])
	tweet = re.sub("</a>", "", tweet)
	to_fd.write(tweet)
	to_fd.write("\n")

to_fd.flush()
to_fd.close()