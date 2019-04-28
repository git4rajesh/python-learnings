from itertools import chain, combinations, product
from collections import OrderedDict


class CombinationGen:
    def __init__(self, yaml_n_wise_dct):
        self.yaml_n_wise_dct = yaml_n_wise_dct
        self.lst_master = []

    def generate_combination(self, n_wise, len_yaml_full_dct, yaml_key_index_dct):
        lst_merged_yaml_vals = []

        counter = 0
        lst_min_item = []
        temp_yaml_key_index_dct = yaml_key_index_dct.copy()
        self.sorted_yaml_key_index_dct = OrderedDict()

        # Logic to sort the yaml_key_index_dct and use the sorted dct during populating empty list
        # Logic to create a list of items ascending order
        while counter < len(yaml_key_index_dct):
            min_item = min(temp_yaml_key_index_dct, key=temp_yaml_key_index_dct.get)
            self.sorted_yaml_key_index_dct[min_item] = yaml_key_index_dct[min_item]
            del temp_yaml_key_index_dct[min_item]
            lst_min_item.append(min_item)
            counter += 1

        # We get the minimum index value first in combination so that the order is maintained in created Combination
        for item in lst_min_item:
            lst_merged_yaml_vals += self.yaml_n_wise_dct[item]

        lst_full_combination = list(combinations(lst_merged_yaml_vals, n_wise))
        combination_lst_of_tup = self.remove_uncovered_combinations(lst_full_combination)
        lst_final_combination = [list(item) for item in combination_lst_of_tup]

        # print('The length of the combination is : {}\n'.format(len(lst_final_combination)))
        # print('The Combination list is : {}\n'.format(lst_final_combination))

        for item in lst_final_combination:
            self.create_empty_list(item, len_yaml_full_dct)

        # print('The length of master list is', len(self.lst_master))
        # print('The combination list with values inserted at correct index', self.lst_master)
        return self.lst_master

    def remove_uncovered_combinations(self, lst_full_combination):
        lst_temp_combination = lst_full_combination.copy()

        for field in self.yaml_n_wise_dct:
            field_values = set(self.yaml_n_wise_dct[field])
            for item in lst_full_combination:
                common_values = set(item).intersection(field_values)
                if len(common_values) > 1 and item in lst_temp_combination:
                    lst_temp_combination.remove(item)
        return lst_temp_combination

    def create_empty_list(self, item, len_yaml_full_dct):
        # Logic to create a list having holes and with values populated from combination_lst at correct index
        lst_empty = [''] * len_yaml_full_dct
        for index, val in enumerate(item):
            pos_for_item = list(self.sorted_yaml_key_index_dct.values())[index]
            lst_empty[pos_for_item] = val
        self.lst_master.append(lst_empty)
