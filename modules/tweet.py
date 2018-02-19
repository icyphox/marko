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
    
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()

def get_history(user):
    all_tweets = []
    filepath = '%s_timeline' % (user)
   
    try:
        progress = 
        for status in tqdm(tweepy.Cursor(api.user_timeline, screen_name=user).items()):
             all_tweets.append(status)            
    except KeyboardInterrupt:
        out_tweets = [tweet.text.encode('utf-8') for tweet in all_tweets]
        with open(filepath, 'w') as f:
            f.write(str(out_tweets))
        return filepath
