my_dct = {'first': 1, 'second': 2, 'third': 3}

rank_dict = {rank: name for name, rank in my_dct.items()}
print(rank_dict, type(rank_dict))

chile_len_set = {len(name) for name in rank_dict.values()}

print(chile_len_set, type(chile_len_set))

