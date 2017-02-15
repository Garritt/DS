import sys
import json
import tweepy

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


# GETS A DAYS WORTH OF TWEETS FROM USERNAME. 
#
# returns False if it must keep scraping tweets, True if it has finished

def get_tweets(username, num_tweets):

	tweets_dict = {}

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	

	# Scraping with Tweepy
	tweets = api.user_timeline(screen_name = username, count = num_tweets)
	for tweet in tweets:
		tweet_date_time = str(tweet.created_at).split()
		tweet_date = tweet_date_time[0]
		tweet_time = tweet_date_time[1]
		tweet_text = tweet.text
		if tweets_dict.get(tweet_date) == None:
			tweets_dict[tweet_date] = {}
			tweets_dict[tweet_date][tweet_time] = tweet_text
		else:
			tweets_dict[tweet_date][tweet_time] = tweet_text

	
	with open('tweet_db.json') as datafile:
		data = json.load(datafile)
	data[username] = tweets_dict
	with open('tweet_db.json', 'w') as datafile:
		json.dump(data, datafile, indent = 2)




get_tweets('realDonaldTrump', 200)