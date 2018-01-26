import tweepy, os

def tweepy_auth():
    if os.path.isfile('consumer.py'):
        import consumer
        auth = tweepy.OAuthHandler(consumer.C_KEY, consumer.C_SECRET) 
        auth.set_access_token(consumer.A_TOKEN, consumer.A_SECRET)

    else:
# api keys exported in virtualenv
        A_TOKEN = os.environ['A_TOKEN']
        A_SECRET = os.environ['A_SECRET']
        C_KEY = os.environ['C_KEY']
        C_SECRET = os.environ['C_SECRET']

        auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
        auth.set_access_token(A_TOKEN, A_SECRET)

    api = tweepy.API(auth) 
    return api

