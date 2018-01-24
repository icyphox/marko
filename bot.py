import tweepy
import os

# api keys exported in virtualenv
A_TOKEN= os.environ['A_TOKEN']
A_SECRET = os.environ['A_SECRET']
C_KEY = os.environ['C_KEY']
C_SECRET = os.environ['C_SECRET']

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_SECRET)

api = tweepy.API(auth) 

def do_tweet():
    with open('topkek.txt') as f:
        for line in f:
            twt_txt = '[icybot] https://github.com/icyphox/icybot\n --- \n' + line 
            print(twt_txt)

do_tweet()
