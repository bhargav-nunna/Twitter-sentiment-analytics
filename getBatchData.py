import tweepy
from tweepy import OAuthHandler
from accessConfig import *
import json
import codecs
import boto3
import logging
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
queryHashtag = 'DonaldTrump'

def process_or_store(tweet):
    #print(json.dumps(tweet))
    f = codecs.open('tweetDump.json', 'a','utf-8')
    try:
        response = firehose_client.put_record(
            DeliveryStreamName='veera-twitter-data-stream',
            Record={
                'Data': json.dumps(tweet, ensure_ascii=False, encoding="utf-8")
            }
        )
        logging.info(response)
    except Exception:
        logging.exception("Problem pushing to firehose")
    f.write(json.dumps(tweet, ensure_ascii=False, encoding="utf-8")+'\n')
    f.close()



firehose_client = boto3.client('firehose', region_name="us-west-2")
LOG_FILENAME = 'Twitter-sentiment-analytics.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

for tweet in tweepy.Cursor(api.search, q=queryHashtag).items(100):
	process_or_store(tweet._json)


