import tweepy
import os
import markovify
import time

# api keys exported in virtualenv
A_TOKEN= os.environ['A_TOKEN']
A_SECRET = os.environ['A_SECRET']
C_KEY = os.environ['C_KEY']
C_SECRET = os.environ['C_SECRET']

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_SECRET)

api = tweepy.API(auth) 

with open('lotr.txt') as f:
    text = f.read()

text_model = markovify.Text(text)


def construct_twt():
    while True:
        markov_text = text_model.make_short_sentence(140)
        if '`' or '"' not in text_model:
            twt_txt = '[icybot] https://github.com/icyphox/icybot \n' + markov_text
            print(twt_txt)
            time.sleep(5)

construct_twt()
