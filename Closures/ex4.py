# Using lambda


# def startAt(start):
#     def invisible(inc):
#         return start + inc
#     return invisible
#
# f = startAt(10)
# g = startAt(100)
#
# print(f(5))
# print(g(2))


def start_at(start):
    return lambda inc: start + inc

f = start_at(10)
g = start_at(100)

print(f(5))
print(g(2))

