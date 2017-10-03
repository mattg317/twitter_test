# Dependencies
import tweepy
import time
import json
import os


# Twitter API Keys
consumer_key = os.environ.get('consumer_key')
consumer_secret = os.environ.get('consumer_secret')
access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

counter = 0


def tweet_out(count):

    api.update_status("This is a tweet at " + str(count))
    print(f"{count} Status updated")


while(True):
    tweet_out(counter)
    counter += 1
    time.sleep(60)
