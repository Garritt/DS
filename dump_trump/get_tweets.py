import time
import sys
import json
import tweepy

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

todays_tweets = {}

# GETS A DAYS WORTH OF TWEETS FROM USERNAME. 
#
# returns False if it must keep scraping tweets, True if it has finished

def get_tweets(username, num_tweets):

	finished = True
	todays_date = str(time.strftime("%Y-%m-%d"))

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	# Scraping with Tweepy
	tweets = api.user_timeline(screen_name = username, count = num_tweets)
	count = 0
	for tweet in tweets:
		count+=1
		tweet_date_time = str(tweet.created_at).split()
		tweet_date = tweet_date_time[0]
		tweet_time = tweet_date_time[1]
		if tweet_date == todays_date:
			todays_tweets[tweet_time] = tweet.text
			if count is num_tweets:
				finished = False

	if finished:
		with open('tweet_db.json') as datafile:
			data = json.load(datafile)
		data[username][todays_date] = todays_tweets
		with open('tweet_db.json', 'w') as datafile:
			json.dump(data, datafile, indent = 2)
	else:
		return finished

if __name__ == '__main__':

	num_tweets = 3

	if len(sys.argv) == 2:
		while get_tweets(argv[1], num_tweets) is False:
			num_tweets += 10
	else:
		while get_tweets('realDonaldTrump', num_tweets) is False:
			num_tweets += 10
		#print('Usage: python3 get_tweets username')
