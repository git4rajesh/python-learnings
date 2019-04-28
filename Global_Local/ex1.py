import math

money = 2000


def add_money():
    global money  # Access the global variable with prefix global.
    local_money = 10
    money += 1


def get_scope():
    local_money = 10
    global money
    # Methods globals() and locals() used to get the scopes of variables
    print('>>>> Globals', globals())
    print('>>>>Locals', locals())


# print(money)
add_money()
print(money)
#
#
# print(dir(math))
# print(help(math.ceil))
#
# print(__file__)

get_scope()
