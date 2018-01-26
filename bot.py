import tweepy, os, markovify, time, sys, argparse
import urllib.request
from inscriptis import get_text

if open('consumer.py'):
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
            print('\033[33m' + '[+] Parsing text file.')
            text = f.read()
    elif args.url:
        url = args.url
        print('\033[33m' + '[+] Parsing specified URL.')
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent,}
        request = urllib.request.Request(url,None,headers)
        html = urllib.request.urlopen(request).read().decode('utf-8')
        text = get_text(html)
    model = markovify.Text(text)
    print('\033[33m' + '[+] Generating a model.')
    return model

# marokvify's the model and generates txt for a tweet
def construct_twt(text_model):
    print('\033[33m' + '[+] Attempting to generate a Markov chain.')
    markov_text = text_model.make_short_sentence(140)
    if markov_text == None:
        print('\033[91m' + '[!] Failed to generate a Markov chain. Exiting.')
        sys.exit(1)
    else:
        print('\033[33m' + '[+] Constructing your tweet.')
        if '`' or '"' not in text_model:
            twt_txt = '[icybot]\n'  + markov_text
        return twt_txt

# tweets it
def do_tweet(text):
    api.update_status(text)
    print('\033[36m' + '[*] Tweet sent.')

def main():
    model = gen_textmodel()
    tweet_text = construct_twt(model)
    do_tweet(tweet_text) 

if __name__ == "__main__":
    main()
