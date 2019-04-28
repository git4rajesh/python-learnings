from rest_request.leankit import jediqa_token
import requests

url = 'https://jediqa.leankit.com/io/card/696317626'
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(jediqa_token) }

r = requests.get(url, headers=headers)

print(r.content)

