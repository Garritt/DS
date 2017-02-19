from twython import Twython # pip3 install twython
from pprint import pprint
import time as t 
import json

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

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
    user_timeline = twitter.get_user_timeline(screen_name=username,count=200, include_retweets=False, max_id=lis[-1])
    t.sleep(5) ## 5 minute rest between api calls
    for tweet in user_timeline:
        created_at = tweet['created_at']
        ca_list = str(created_at).split()
        month = ca_list[1]
        month_ec = months[month]
        year = ca_list[5]
        date = ca_list[2]
        time = ca_list[3]
        day_format = year + "-" + month_ec + "-" + date
        lis.append(tweet['id'])
        if tweets_dict.get(day_format) == None:
        	tweets_dict[day_format] = {}
        tweets_dict[day_format][time] = tweet['text']

with open('tweet_db.json') as datafile:
	data = json.load(datafile)
data[username] = tweets_dict
with open('tweet_db.json', 'w') as datafile:
	json.dump(data, datafile, indent = 2)