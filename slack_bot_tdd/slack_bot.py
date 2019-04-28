import time
from slackclient import SlackClient

token = 'xoxb-6920022771-371249136274-C33mopzABmm8IkaRp59Wp9wk'

slack_client = SlackClient(token)

def slack_connect():
    return slack_client.rtm_connect()


def slack_read_rtm():
    while True:
        print(slack_client.rtm_read())
        time.sleep(1)

# slack_connect()
# slack_read_rtm()