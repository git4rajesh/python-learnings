my_lst = list(range(1, 1001))


def my_gen(batch_size=200):
    global GLOBAL_COUNTER
    local_counter = 0
    lst_output = []
    while GLOBAL_COUNTER <= 1000:
        if local_counter < batch_size:
            lst_output.append(my_lst[GLOBAL_COUNTER])
            local_counter += 1
            GLOBAL_COUNTER +=1
        else:
            yield lst_output
            local_counter = 0
            lst_output = []

GLOBAL_COUNTER = 0
print(next(my_gen()))
# print(GLOBAL_COUNTER)
# print(next(my_gen()))
# print(GLOBAL_COUNTER)
# print(next(my_gen()))
# print(GLOBAL_COUNTER)
# print(next(my_gen()))
# print(GLOBAL_COUNTER)
# print(next(my_gen()))
# print(GLOBAL_COUNTER)

# GLOBAL_COUNTER = 0
# for batch in my_gen():
#     print(batch)
#     print(GLOBAL_COUNTER)

