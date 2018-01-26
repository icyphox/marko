import tweepy, os, markovify, time, sys, argparse
import urllib.request
from inscriptis import get_text

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

def gen_textmodel():
    if args.file:
        with open(args.f) as f:
            print('[+] Parsing text file.')
            text = f.read()
    elif args.url:
        url = args.url
        print('[+] Parsing specified URL.')
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent,}
        request = urllib.request.Request(url,None,headers)
        html = urllib.request.urlopen(request).read().decode('utf-8')
        text = get_text(html)
    model = markovify.Text(text)
    print('[+] Generating a model.')
    return model

def construct_twt(text_model):
    print('[+] Attempting to generate a Markov chain.')
    markov_text = text_model.make_short_sentence(140)
    if markov_text == None:
        print('[!] Failed to generate a Markov chain. Exiting.')
        sys.exit(1)
    else:
        print('[+] Constructing your tweet.')
        if '`' or '"' not in text_model:
            twt_txt = '[icybot]\n'  + markov_text
        return twt_txt

def do_tweet(text):
    api.update_status(text)
    print('[*] Tweet sent.')

def main():
    model = gen_textmodel()
    tweet_text = construct_twt(model)
    do_tweet(tweet_text) 

if __name__ == "__main__":
    main()
    

