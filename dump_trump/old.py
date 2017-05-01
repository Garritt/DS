from twython import Twython # pip3 install twython
from pprint import pprint
from datetime import datetime
import time as t 
import json

CONSUMER_KEY = '5kdwernp3J3Sf4zZGBfXPaym6'
CONSUMER_SECRET = 's5UcGtDe0at4UT0issQMw4WNnAaflBgRXuFywPOIP4GUoaUx9v'
ACCESS_KEY = '244624131-5xjNt6AZnfAYzYxapzQCuqkIe4lmzYmrxaQJUl6v'
ACCESS_SECRET = 'kji5k5v9eYlGnsBJa3Rwum7P1rKhdH3IUNoH6uHIOiSEW'

username = 'realDonaldTrump'
tweets_dict = {}

months = {
	'Jan': '01',
	'Feb': '02',
	'Mar': '03',
	'Apr': '04',
	'May': '05',
	'Jun': '06',
	'Jul': '07',
	'Aug': '08',
	'Sep': '09',
	'Oct': '10',
	'Nov': '11',
	'Dec': '12'
}

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
user_timeline = twitter.get_user_timeline(screen_name=username, count=1) ## this is the latest starting tweet id
t_id = user_timeline[0]['id']
lis = list()
lis.append(t_id)

for i in range(0, 16): ## iterate through all tweets
## tweet extract method with the last list item as the max_id
    user_timeline = twitter.get_user_timeline(screen_name=username, count=200, include_retweets=False, max_id=lis[-1])
    t.sleep(150) ## 5 minute rest between api calls
    
    last_tweet_time = None
    for tweet in reversed(user_timeline):
        created_at = tweet['created_at']
        created_at_f = created_at.split("+")[0]
        created_at_f = created_at_f[4:]
        ca_list = str(created_at).split()
        month = ca_list[1]
        month_ec = months[month]
        year = ca_list[5]
        date = ca_list[2]
        time = ca_list[3]
        created_at_f = year + " "+ str(created_at_f)
        datetime = datetime.strptime(created_at_f, '%Y %b %d %H:%M:%S ')
        day_format = year + "-" + month_ec + "-" + date
        lis.append(tweet['id'])
        if tweets_dict.get(day_format) == None:
        	tweets_dict[day_format] = {}
        tweets_dict[day_format][time] = {}
        tweets_dict[day_format][time]['text'] = tweet['text']
        tweets_dict[day_format][time]['favorites'] = tweet['favorite_count']
        tweets_dict[day_format][time]['retweets'] = tweet['retweet_count']
        tweets_dict[day_format][time]['created_at'] = str(datetime)
        tweets_dict[day_format][time]['label'] = None
        try:
        	time_since_last_tweet = datetime - last_tweet_time
        except TypeError:
        	time_since_last_tweet = None
        tweets_dict[day_format][time]['time_since_last_tweet'] = str(time_since_last_tweet)
        last_tweet_time = datetime


with open('tweet_db.json') as datafile:
	data = json.load(datafile)
data[username] = tweets_dict
with open('tweet_db.json', 'w') as datafile:
	json.dump(data, datafile, indent = 2)



