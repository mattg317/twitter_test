# Dependencies
import tweepy
import time
import json
#from keys import key as keys


# Twitter API Keys
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

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
    time.sleep(5)
