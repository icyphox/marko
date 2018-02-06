import tweepy, os.path, sys, json
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

    filename = user[1:] + '.txt'
    all_tweets = []
    path = 'timelines/' + filename

    new_tweets = api.user_timeline(screen_name=user,count=200)
    all_tweets.extend(new_tweets)
    oldest = all_tweets[-1].id - 1
    i = len(new_tweets)
    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(screen_name=user,count=200,max_id=oldest)
        all_tweets.extend(new_tweets)
        oldest = all_tweets[-1].id - 1
        progress(i, len(all_tweets, '[+] Downloading tweets.'))
        i -= 1

    out_tweets = [tweet.text.encode('utf-8') for tweet in all_tweets]
    
    if not os.path.exists('timelines'):
        os.makedirs('timelines')

    with open(path, 'w') as f:
        for tweet in out_tweets:
            f.write(tweet.decode('utf-8'))

    return path
