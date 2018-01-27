import tweepy
import marko

def do_tweet(text):
    tweet = api.update_status(text)
    print(Fore.CYAN + '[*] Tweet can be found at https://twitter.com/' + api.me().screen_name  + '/status/' + tweet.id_str)

def get_history(user):
    for status in tweepy.Cursor(api.user_timeline, screen_name=user).items():
        return status._json
