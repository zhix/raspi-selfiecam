#!/usr/bin/env python3

from twython import Twython, TwythonError
import time

## Twitter account = ChumbakaAsia

CONSUMER_KEY = 'T________________________________________p'
CONSUMER_SECRET = 'pJwdQmOjr___________________________kQz'
ACCESS_KEY = '4________________________________________ta'
ACCESS_SECRET = 'lxtu7_________________________________UkL'

print("Getting ready...")

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

try:
    twitter.update_status(status='Greetings from our Python script!')
    print("Status updated.")
except TwythonError as e:
    print(e)
