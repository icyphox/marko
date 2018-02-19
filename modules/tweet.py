import tweepy, os.path, sys, json, signal
from tqdm import tqdm
from colorama import Fore, init
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
import marko, auth

init(autoreset=True)

api = auth.tweepy_auth()

def do_tweet(text):
    tweet = api.update_status(text)
    print(Fore.CYAN + '[*] Tweet can be found at https://twitter.com/' + api.me().screen_name  + '/status/' + tweet.id_str)

def get_history(user):
    all_tweets = []
    filepath = '%s_timeline' % (user)
   
    try:
        for status in all_tweets:
            print(Fore.GREEN + '\n[+] %d tweets fetched.' % len(all_tweets), end='')
            all_tweets.append(status)            
    except KeyboardInterrupt:
        out_tweets = [tweet.text.encode('utf-8') for tweet in all_tweets]
        with open(filepath, 'w') as f:
            f.write(str(out_tweets))
        return filepath
