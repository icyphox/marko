<center><img src='https://xix.ph0x.me/marko.png'></center>

# A Twitter bot that tries to sound smart. 
[![Coverage Status](https://coveralls.io/repos/github/icyphox/Marko/badge.svg?branch=master)](https://coveralls.io/github/icyphox/Marko?branch=master)
[![Build Status](https://travis-ci.org/icyphox/Marko.svg?branch=master)](https://travis-ci.org/icyphox/Marko)



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

	usage: bot.py [-h] [--file FILE] [--url URL] [--handle HANDLE]
              [--gen-from-user GEN_FROM_USER]

	A Twitter bot that tweets Markov chains.

	optional arguments:
	  -h, --help            show this help message and exit
	  --file FILE           path to text file (.txt)
	  --url URL             url to generate a model from
	  --handle HANDLE       twitter handle of user to tweet at
	  --gen-from-user GEN_FROM_USER
                        generate text model from user's timeline

