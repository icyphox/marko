import tweepy, os, markovify, time, sys, argparse, requests
from inscriptis import get_text
from colorama import Fore, init

# colorama autoreset
init(autoreset=True)

if os.path.isfile('consumer.py'):
    import consumer
else:
# api keys exported in virtualenv
    A_TOKEN= os.environ['A_TOKEN']
    A_SECRET = os.environ['A_SECRET']
    C_KEY = os.environ['C_KEY']
    C_SECRET = os.environ['C_SECRET']

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_SECRET)

api = tweepy.API(auth) 

# get file path from args
parser = argparse.ArgumentParser(description='A Twitter bot that tweets Markov chains.')
parser.add_argument('-f', '--file', help='path to text model (.txt)')
parser.add_argument('-u', '--url', help='urlto generate a model from')

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)
args = parser.parse_args()

# generates text model from either a text file or URL
def gen_textmodel():
    if args.file:
        with open(args.f) as f:
            print(Fore.GREEN + '[+] Parsing text file.') 
            text = f.read()

    elif args.url:
        url = args.url
        print(Fore.GREEN + '[+] Parsing specified URL.')
        r = requests.get(url)
        text = get_text(r.text)
    model = markovify.Text(text)
    print(Fore.GREEN + '[+] Generating a model.')
    return model

# marokvify's the model and generates txt for a tweet
def construct_twt(text_model):
    print(Fore.GREEN + '[+] Attempting to generate a Markov chain.')
    markov_text = text_model.make_short_sentence(140)
    if markov_text == None:
        print(Fore.RED + '[!] Failed to generate a Markov chain. Exiting.')
        sys.exit(1)
    else:
        print(Fore.GREEN + '[+] Constructing your tweet.')
        if '`' or '"' not in text_model:
            twt_txt = '[Marko]\n'  + markov_text
        return twt_txt

# tweets it
def do_tweet(text):
    tweet = api.update_status(text)
    print(Fore.CYAN + '[*] Tweet can be found at https://twitter.com/' + api.me().screen_name  + '/status/' + tweet.id_str )
    
def main():
    model = gen_textmodel()
    tweet_text = construct_twt(model)
    do_tweet(tweet_text) 

if __name__ == "__main__":
    main()
