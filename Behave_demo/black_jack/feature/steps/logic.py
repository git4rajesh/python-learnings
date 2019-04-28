import sys
import os
path = os.path.join(os.path.dirname(__file__), '../../../..')
sys.path.extend([path])

from behave import *
from Behave_demo.black_jack.blackjack import Dealer


@given('a dealer')
def step_impl(context):
    context.dealer = Dealer()
    print('>>>>',context.mylist)
    assert(3 == len(context.mylist))


@when('the round starts')
def step_impl(context):
    context.dealer.new_round()
    assert ((2 == context.mylist[1]) and (1 == context.mydict['a']))


@then('the dealer gives itself two cards')
def step_impl(context):
    assert (len(context.dealer.hand) == 2)


@then('first card is A-claver')
def step_impl(context):
    context.response = 'Raj'
    assert (context.dealer.hand[0] == 'A-claver')


@then('second card is "{secondcard}"')
def step_impl(context, secondcard):
    print('>>>>', secondcard)
    assert (context.dealer.hand[1] == secondcard)


@then('card number is "{num:d}"')
def step_impl(context, num):
    assert (num == context.dealer.card_num)


@then('use context')
def step_impl(context):
    assert (context.response == 'Raj')

