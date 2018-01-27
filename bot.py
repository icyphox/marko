import tweepy, sys, argparse
from modules import auth, markov
from colorama import Fore, init

# colorama autoreset
init(autoreset=True)

# auth
api = auth.tweepy_auth()

# get file path from args
parser = argparse.ArgumentParser(description='A Twitter bot that tweets Markov chains.')
parser.add_argument('--file', help='path to text file (.txt)')
parser.add_argument('--url', help='url to generate a model from')
parser.add_argument('--handle', help='twitter handle of user to tweet at')

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)
args = parser.parse_args()

# tweets it
def do_tweet(text):
    tweet = api.update_status(text)
    print(Fore.CYAN + '[*] Tweet can be found at https://twitter.com/' + api.me().screen_name  + '/status/' + tweet.id_str )
    
def main():
    if args.file:
        model = markov.gen_textmodel(f=args.file)
    elif args.url:
        model = markov.gen_textmodel(u=args.url)

    if args.handle:
        tweet_text = markov.construct_twt(model, args.handle)
    else:
        tweet_text = markov.construct_twt(model)

    do_tweet(tweet_text) 

if __name__ == "__main__":
    main()
