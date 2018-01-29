# Marko
A Twitter bot that tries to sound smart.

### Installation
If you want to run this under your own account, follow these steps:
- clone this repo
- [create your own Twitter Application](https://apps.twitter.com/app/new)
- get your access token, access token secret, consumer token and consumer secret
- export them as shell variables `A_TOKEN`, `A_SECRET`, `C_KEY` and `C_SECRET` respectively

 **OR**

- create a `consumer.py` in the same directory with the contents like so:
```python
# you know what goes where

A_TOKEN = ''    
A_SECRET = ''
C_KEY = ''
C_SECRET = ''
```
- finally

```$ pip install -r requirements.txt```


### Usage

	usage: bot.py [-h] [-f FILE] [-u URL]

	A Twitter bot that tweets Markov chains.

	optional arguments:
	 -h, --help            show this help message and exit
	-f FILE, --file FILE  path to text model (.txt)
	-u URL, --url URL     urlto generate a model from

