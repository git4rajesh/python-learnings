from requests_oauthlib import OAuth1

class Oauth_Gen:

    def __init__(self):
            self.CLIENT_KEY = '2fbf522ed6ba4f07723f9347d6aaf2c3'
            self.CLIENT_SECRET = '6d6d7d95edacc1e7a337ae26792c41d9844054ba'
            self.access_token_key = 'bd30188e8959094ada5e184fcf850d6b'
            self.access_token_secret = '02cacf3cb22666759df7484323f671c666972b63'


    def get_oauth(self):
            oauth = OAuth1(self.CLIENT_KEY, client_secret=self.CLIENT_SECRET, resource_owner_key=self.access_token_key,
                           resource_owner_secret=self.access_token_secret)
            return oauth