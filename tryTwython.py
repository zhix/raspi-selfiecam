#!/usr/bin/env python3

from twython import Twython, TwythonError
import time

## Twitter account = ChumbakaAsia

CONSUMER_KEY = 'TaqYW2bVCtBqoT03blDN5Fslp'
CONSUMER_SECRET = 'pJwdQmOjrdyuu13ZaqkcqCrSL6JAPjhNV34FnKPMzFRDfhXkQz'
ACCESS_KEY = '4900136473-pGYV6hO8jWgPFbViaxnLhl1766fwTw7uDef24ta'
ACCESS_SECRET = 'lxtu7VsSi3aPSLEZ1Gyq4pN6iNdkSNxpaLmR6LbD8fUkL'

print("Getting ready...")

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

try:
    twitter.update_status(status='Greetings from our Python script!')
    print("Status updated.")
except TwythonError as e:
    print(e)
