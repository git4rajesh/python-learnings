#!/usr/bin/env python

import requests
from requests_oauthlib import OAuth1 as OAuth
from urllib.parse import parse_qs
import webbrowser
import json

CLIENT_KEY = u'2fbf522ed6ba4f07723f9347d6aaf2c3'
CLIENT_SECRET = u'6d6d7d95edacc1e7a337ae26792c41d9844054ba'
# BASE_URL = u'https://api-pptest.projectplace.com/'
BASE_URL = u'https://rnd3.demo.projectplace.com/'

# If you already have an access token and secret, fill those in here. That will bypass the whole authentication
# flow and allow you to issue requests immediately. (I.e if you have a robot account or an already authenticated user.

access_token_key =  None
access_token_secret = None

if access_token_key is None:
    print('Getting request token...:')
    oauth = OAuth(CLIENT_KEY, client_secret=CLIENT_SECRET)
    print (oauth)
    r = requests.post(BASE_URL + 'initiate', auth=oauth)
    credentials = parse_qs(r.content)
    request_token_key = credentials.get(b'oauth_token')[0].decode('ascii')
    request_token_secret = credentials.get(b'oauth_token_secret')[0].decode('ascii')
    print(request_token_key, 'with secret', request_token_secret)

    print("Opening webbrowser to authenticate request token")
    webbrowser.open(BASE_URL + '/authorize?oauth_token=' + request_token_key)
    oauth_verifier = input('Input oauth_verifier: ')

    print("Exchanging request token for access token")
    oauth = OAuth(CLIENT_KEY, client_secret=CLIENT_SECRET, resource_owner_key=request_token_key,
                  resource_owner_secret=request_token_secret, verifier=oauth_verifier)
    r = requests.post(BASE_URL + 'token', auth=oauth)
    credentials = parse_qs(r.content)
    access_token_key = credentials.get(b'oauth_token')[0].decode('ascii')
    access_token_secret = credentials.get(b'oauth_token_secret')[0].decode('ascii')

    print("Successfully fetch access token", access_token_key, 'with secret', access_token_secret)

print('Getting user profile...')
oauth = OAuth(CLIENT_KEY, client_secret=CLIENT_SECRET, resource_owner_key=access_token_key,
              resource_owner_secret=access_token_secret)
r = requests.get(url=BASE_URL + 'api/v1/user/me/profile', auth=oauth)
print(json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': ')))