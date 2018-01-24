import tweepy
import os
import markovify
import threading

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

while True:
    if 
