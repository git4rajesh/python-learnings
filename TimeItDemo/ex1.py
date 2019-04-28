import time
import timeit


def my_func():
    time.sleep(10)
    print('Dummy function which returns a value')
    return True


start_time = timeit.default_timer()
print(my_func())
end_time = timeit.default_timer()
print(end_time - start_time)
