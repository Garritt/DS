#!/usr/local/bin/python3

import time
import schedule
import json
import tweepy
import sys

CONSUMER_KEY = '5kdwernp3J3Sf4zZGBfXPaym6'
CONSUMER_SECRET = 's5UcGtDe0at4UT0issQMw4WNnAaflBgRXuFywPOIP4GUoaUx9v'
ACCESS_KEY = '244624131-5xjNt6AZnfAYzYxapzQCuqkIe4lmzYmrxaQJUl6v'
ACCESS_SECRET = 'kji5k5v9eYlGnsBJa3Rwum7P1rKhdH3IUNoH6uHIOiSEW'

todays_tweets = {}

# GETS A DAYS WORTH OF TWEETS FROM USERNAME. 
#
# returns False if it must keep scraping tweets, True if it has finished

def get_tweets():

	#print(" - DOWNLOADING AGENT ORANGE -")
	username = 'realDonaldTrump'
	finished = True
	todays_date = str(time.strftime("%Y-%m-%d"))

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)

	# Scraping with Tweepy (assumes 
	tweets = api.user_timeline(screen_name = username, count = 10)
	for tweet in tweets:
		tweet_date_time = str(tweet.created_at).split()
		tweet_date = tweet_date_time[0]
		tweet_time = tweet_date_time[1]
		if tweet_date == todays_date:
			if todays_tweets.get(tweet_time) == None:
				todays_tweets[tweet_time] = tweet.text

	# with open('tweet_db.json') as datafile:
	# 	data = json.load(datafile)
	# data[username][todays_date] = todays_tweets
	# with open('tweet_db.json', 'w') as datafile:
	# 	json.dump(data, datafile, indent = 2)



get_tweets()

# if __name__ == '__main__':

# 	schedule.every(.1).minutes.do(get_tweets)
# 	while True:
# 		schedule.run_pending()
# 		# 2 hours
# 		time.sleep(100) 

