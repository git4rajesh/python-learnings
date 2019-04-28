def fact_recurs(n):
    if n == 0:
        return 1

    if n == 1:
        return n
    else:
        return n * fact_recurs(n-1)


print(fact_recurs(6))


def fact_linear(n):
    if n == 0:
        return 1
    range_index = n +1
    num = 1
    for value in range(1,range_index):
        num *= value
    return num

print(fact_linear(6))