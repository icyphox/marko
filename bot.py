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

def gen_textmodel():
    with open('lotr.txt') as f:
        text = f.read()
    model = markovify.Text(text)
    return model

def construct_twt(text_model):
    markov_text = text_model.make_short_sentence(140)
    if '`' or '"' not in text_model:
        twt_txt = '[icybot] https://github.com/icyphox/icybot \n' + markov_text
    return twt_txt

def do_tweet(text):
    api.update_status(text)
    time.sleep(1800)
    
def main():
    model = gen_textmodel()
    tweet_text = construct_twt(model)
    do_tweet(tweet_text) 

if __name__ = "__main__":
    main()
    
