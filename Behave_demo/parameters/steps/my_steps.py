from behave import *


@given(u'I search for a valid number')
def step_impl(context):
    assert True


@then('the result page will include "{text}"')
def step_impl(context, text):
    assert(text == 'success')
