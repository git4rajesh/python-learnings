import pytest
from slack_bot_tdd import slack_bot

def test_slack_connect():
    assert(slack_bot.slack_connect() == True)

# @pytest.mark.skip(reason='not developed fully')
def test_slack_read_rtm():
    print(slack_bot.slack_read_rtm())