#!/usr/local/bin/python3

import time
import schedule
import json
import tweepy
import sys

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

todays_tweets = {}

# GETS A DAYS WORTH OF TWEETS FROM USERNAME. 
#
# returns False if it must keep scraping tweets, True if it has finished

def get_tweets():

	#print(" - DOWNLOADING AGENT ORANGE -")
	username = 'realDonaldTrump'
	finished = True
	todays_date = str(time.strftime("%Y-%m-%d"))

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
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

	with open('tweet_db.json') as datafile:
		data = json.load(datafile)
	data[username][todays_date] = todays_tweets
	with open('tweet_db.json', 'w') as datafile:
		json.dump(data, datafile, indent = 2)



if __name__ == '__main__':

	schedule.every(120).minutes.do(get_tweets)
	while True:
		schedule.run_pending()
		# 2 hours
		time.sleep(100) 

