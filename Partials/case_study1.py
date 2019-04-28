import re
lines = "Sample text line"

## *********************************** ##
#         Using  if-else
## ********************************* ##


def search_for_alphabets(text):
    print('Inside some action')


def search_for_integers(text):
    print('Inside some_other_action')


def search_for_others():
    print('Inside default action')


for text in lines.split(' '):
    if re.search("[a-zA-Z]*", text):
     search_for_alphabets(text)
    elif re.search("[1-5]\s\=", text):
     search_for_integers(text)
    else:
     search_for_others()


## *********************************** ##
#         Using  Functions
## ********************************* ##


def regex_for_alphabets(text):
  return re.search("[a-zA-Z]*", text)


def regex_for_integers(text):
  return re.search("[1-5]\s\=", text)


def regex_for_others(text):
  return re.search("pattern_188364625", text)


for text in lines:
  if regex_for_alphabets(text):
    search_for_alphabets(text)
  elif regex_for_integers(text):
    search_for_integers(text)
  else:
    search_for_others()

## *********************************** ##
#         Using  partials
## ********************************* ##

from functools import partial


def my_search_method():
    is_alphabets = partial(re.search, '[a-zA-Z]*')
    is_integers = partial(re.search, '[1-5]\s\=')

    for text in lines:
        if is_integers(text):
            search_for_alphabets(text)
        elif is_alphabets(text):
            search_for_integers(text)
        else:
            search_for_others()