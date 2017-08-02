import tweepy
from tweepy import OAuthHandler
from accessConfig import *
import json
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
queryHashtag = 'DonaldTrump'

def process_or_store(tweet):
    print(json.dumps(tweet))

#for status in tweepy.Cursor(api.home_timeline).items(10):
	# Process a single status
#	process_or_store(status._json) 


for tweet in tweepy.Cursor(api.search, q=queryHashtag).items(100):
	process_or_store(tweet._json)

