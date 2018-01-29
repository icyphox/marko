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

def get_history(user):
    filename = user[1:] + '.txt'
    path = 'timelines/' + filename
#    for status in tweepy.Cursor(api.user_timeline, screen_name=user).items():
#         if not os.path.exists('timelines'):
#            os.makedirs('timelines')
#            with open(path, 'w') as f:
#                print(status._json['text'])
#                f.write(json.dumps(status._json))
#                f.write('\n')
#        else:
#            with open(path, 'w') as f:
#                print(status._json['text'])
#                f.write(json.dumps(status._json))
#                f.write('\n')
# 
    return path
