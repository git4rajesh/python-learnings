import time
import asyncio

def is_prime(nr_num):
    status = True
    for dr_num in range(2, nr_num - 1):
        if (nr_num // dr_num == nr_num/dr_num):
                status = False
                break
    return status


async def highest_prime_below(num):
    print('Highest Prime below number {}'.format(num))

    for nr_num in range(num-1, 0, -1):
        if(is_prime(nr_num)):
            print('    -> The highest prime below number {} is {}'.format(num, nr_num))
            return nr_num
        await asyncio.sleep(0.01)
        # time.sleep(0.01)


async def main():
    t0 = time.time()
    await asyncio.wait([
        highest_prime_below(100000),
        highest_prime_below(10000),
        highest_prime_below(1000)
        ])
    t1 = time.time()

    print('Took this {} milli seconds'.format(t1-t0))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
