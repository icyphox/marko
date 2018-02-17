import tweepy, sys, argparse
from modules import auth, marko, tweet
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
parser.add_argument('--gen-from-user', help='generate text model from user\'s timeline')

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)
args = parser.parse_args()
    
def main():
    if args.handle:
        if args.file:
            markov_text = marko.gen_markov(f=args.file)
            tweet_text = marko.construct_twt(markov_text, handle=args.handle)
        elif args.url:
            markov_text = marko.gen_markov(u=args.url)
            tweet_text = marko.construct_twt(markov_text, handle=args.handle)
    
    elif args.gen_from_user:
        filepath = tweet.get_history(args.gen_from_user)
        markov_text = marko.gen_markov(f=filepath)
        tweet_text = marko.construct_twt(markov_text)

    else:
        if args.file:
            markov_text = marko.gen_markov(f=args.file)
            tweet_text = marko.construct_twt(markov_text)
        elif args.url:
            markov_text = marko.gen_markov(u=args.url)
            tweet_text = marko.construct_twt(markov_text)

#    elif args.file and args.url:
#       print('[!] Cannot parse from two sources. Aborting.')
# TODO fix ^

    tweet.do_tweet(tweet_text) 

if __name__ == "__main__":
    main()
