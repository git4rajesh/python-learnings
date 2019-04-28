import traceback

# def list_square_nos(list_numbers):
#         result_list = []
#         for number in list_numbers:
#             result_list.append(number * number)
#         return result_list

# print(list_square_nos(list_numbers= [1,2,3,4]))

def gen_square_nos(list_numbers):
    for number in list_numbers:
        yield (number * number)

gen_object = gen_square_nos(list_numbers= [1,2,3,4])
print(gen_object)

# for squares in gen_object:
#     print('Squares', squares)

print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
try:
    print(next(gen_object))
except:
    print(traceback.format_exc())


# def list_comprehension(list_numbers):
#     return [num * num for num in list_numbers]
#
# print(list_comprehension(list_numbers= [1,2,3,4]))


# def generator_comprehension(list_numbers):
#     return (num * num for num in list_numbers)
#
# print(generator_comprehension(list_numbers= [1,2,3,4]))

# for num in generator_comprehension(list_numbers= [1,2,3,4]):
#     print(num)
#
# print('Converting generator to a list', list(generator_comprehension(list_numbers= [1,2,3,4])))

print('End')