from itertools import chain
from Hack_A_Week.input_reader import InputReader
from Hack_A_Week.combination_generator import CombinationGen


class TestCaseGen:
    def __init__(self, n_wise):
        self.n_wise = n_wise
        self.in_reader_obj = InputReader('pict_input.yaml')
        self._initializer()

    def _initializer(self):
        self.yaml_n_wise_dct, self.yaml_key_index_dct = self.in_reader_obj.parse_yaml(self.n_wise)
        print('n-wise dct', self.yaml_n_wise_dct)
        print('n-wise key index', self.yaml_key_index_dct)
        comb_obj = CombinationGen(self.yaml_n_wise_dct)
        len_yaml_full_dct = self.in_reader_obj.len_yaml_full_dct

        self.lst_paired_combination = comb_obj.generate_combination(self.n_wise, len_yaml_full_dct,
                                                                    self.yaml_key_index_dct)

        self.occurence_count = self.get_occurence_count()

    def get_occurence_count(self):
        lst_flattened_combination = list(chain(*self.lst_paired_combination))

        for item in self.yaml_n_wise_dct:
            return lst_flattened_combination.count(self.yaml_n_wise_dct[item][0])

    def distribute_field_values(self):
        self.lst_master = self.lst_paired_combination.copy()
        yaml_full_dct = self.in_reader_obj.yaml_full_dct

        # Loop through the all yaml file fields
        for o_index, val in enumerate(yaml_full_dct):

            if o_index not in self.yaml_key_index_dct.values() and val != 'Ignore Values':  # Start from fields not considered for n-wise

                outer_index = 0
                combination_temp = []

                # Loop the whole paired combination list generated in batches
                for index in range(self.occurence_count, len(self.lst_paired_combination) + 1, self.occurence_count):
                    field_val_index = 0

                    # Loop until it reaches the batch size
                    while outer_index <= index - 1:
                        # removing the holes in the paired combination list
                        s_paired_combination = sorted(set(self.lst_paired_combination[outer_index]),
                                                      key=self.lst_paired_combination[outer_index].index)
                        s_paired_combination.remove('')
                        lst_combination_item = list(s_paired_combination)

                        field_val, field_val_index = self.get_field_val_index(field_val_index, yaml_full_dct[val],
                                                                              combination_temp, lst_combination_item)

                        # Create a temp combination list by adding a new field value

                        combination_temp.append(
                            self.create_temp_lst(lst_combination_item, field_val))
                        self.lst_master[outer_index][o_index] = field_val
                        outer_index += 1
                        field_val_index += 1
        print('master', self.lst_master)

        if self.in_reader_obj.yaml_full_dct.get('Ignore Values'):
            self.ignore_field_values()
        self.write_out_file()

    def distribute_field_values_old(self):
        yaml_full_dct = self.in_reader_obj.yaml_full_dct
        lst_main = []
        lst_main = self.lst_paired_combination.copy()

        # Loop through the all yaml file fields
        for index, val in enumerate(yaml_full_dct):

            if index >= self.n_wise:  # Start from fields not considered for n-wise

                outer_index = 0
                combination_temp = []

                # Loop the whole paired combination list generated in batches
                for index in range(self.occurence_count, len(self.lst_paired_combination) + 1, self.occurence_count):
                    field_val_index = 0

                    # Loop until it reaches the batch size
                    while outer_index <= index - 1:
                        # removing the holes in the paired combination list
                        s_paired_combination = set(self.lst_paired_combination[outer_index])
                        s_paired_combination.remove('')
                        lst_combination_item = list(s_paired_combination)
                        print('>>>>', lst_combination_item)

                        # Method to get the appropriate field value and its index
                        # field_val, field_val_index = self.get_field_val_index(field_val_index, yaml_full_dct[val],
                        #                                                       combination_temp,
                        #                                                       self.lst_paired_combination[outer_index])

                        field_val, field_val_index = self.get_field_val_index(field_val_index, yaml_full_dct[val],
                                                                              combination_temp, lst_combination_item)

                        # Create a temp combination list by adding a new field value
                        combination_temp.append(
                            self.create_temp_lst(self.lst_paired_combination[outer_index], field_val))

                        outer_index += 1
                        field_val_index += 1
                print(combination_temp)
                self.lst_paired_combination = self.flatten_combination_lst(combination_temp)
                print(self.lst_paired_combination)

    def create_temp_lst(self, combination, val):
        last_elem = combination.pop(-1)
        temp = [last_elem, val]
        combination.append(temp)
        return combination

    def get_field_val_index(self, field_val_index, yaml_field_values, combination_temp, paired_combination):

        # Check if index has reached the end and if so reset to start position
        if field_val_index >= len(yaml_field_values):
            field_val_index = 0
        field_val = yaml_field_values[field_val_index]

        # Check if the incoming temp combination list is not empty
        if combination_temp:
            for item in combination_temp:
                lst_new_combination = []
                lst_new_combination.extend([paired_combination[-1], field_val])

                # Logic to make the distribution Unique
                new_combination = set(lst_new_combination)
                existing_combination = set(item[-1])
                len_existing_combination = len(existing_combination)
                len_intersection_output = len(new_combination.intersection(existing_combination))
                if len_intersection_output == len_existing_combination:
                    field_val_index += 1
                    if field_val_index >= len(yaml_field_values):
                        field_val_index = 0
                    field_val = yaml_field_values[field_val_index]

        return field_val, field_val_index

    # To DO:
    # Can go to helper Class
    # Method to expand the List of Lists
    def flatten_combination_lst(self, combinations):
        temp_combination_lst = []
        for combination in combinations:
            out = list(self.flatten_lst(combination))
            temp_combination_lst.append(out)
        return temp_combination_lst

    def flatten_lst(self, combination):
        for item in combination:
            if type(item) == list:
                for item in self.flatten_lst(item):
                    yield item
            else:
                yield item

    def ignore_field_values(self):
        for ignore_value in self.in_reader_obj.yaml_full_dct['Ignore Values']:
            print(ignore_value)
            for combination_val in self.lst_master:
                s_ignore_value = set(ignore_value)
                s_combination_val = set(combination_val)
                intersection_out = s_ignore_value.intersection(s_combination_val)
                if len(intersection_out) == len(s_ignore_value):
                    self.lst_master.remove(combination_val)
        print('Length final', len(self.lst_master))
        print('Most final', self.lst_master)

    def write_out_file(self):
        self.generate_headers()
        with open('out_test_data.txt', 'w') as fh:
            fh.write(str(self.lst_headers) + '\n\n')
            for item in self.lst_master:
                fh.write(str(item) + '\n')

    def generate_headers(self):
        self.lst_headers = []
        for key in self.in_reader_obj.yaml_full_dct.keys():
            if key not in 'Ignore Values':
                self.lst_headers.append(key)
