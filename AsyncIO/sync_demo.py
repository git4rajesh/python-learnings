import time

def is_prime(number):
    status = True
    for i in range(2, number - 1):
        if (number // i == number / i):
            status = False
            break
    return status


def highest_prime_below(num):
    print('Highest Prime below number {}'.format(num))

    for i in range(num - 1, 0, -1):
        if (is_prime(i)):
            print('    -> The highest prime below number {} is {}'.format(num, i))
            return i
        time.sleep(0.01)


def main():
    highest_prime_below(100000)
    highest_prime_below(10000)
    highest_prime_below(1000)


main()
