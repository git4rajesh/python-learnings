import yaml
import yamlordereddictloader
from collections import OrderedDict


class InputReader:
    def __init__(self, file_name):
        with open(file_name, 'r') as file_handle:
            self.yaml_full_dct = yaml.load(file_handle, Loader=yamlordereddictloader.Loader)
            self.len_yaml_full_dct = len(self.yaml_full_dct)
            if self.yaml_full_dct.get('Ignore Values'):
                self.len_yaml_full_dct -= 1

    def parse_yaml(self, n_wise):
        if n_wise < self.len_yaml_full_dct:  # when n-wise is less than total fields in yaml
            self.compute_length_item()
            yaml_n_wise_dct, yaml_key_index_dct = self.create_n_wise_dct(n_wise)
            return yaml_n_wise_dct, yaml_key_index_dct
        elif n_wise == self.len_yaml_full_dct:  # when n-wise is equal to the total fields in yaml
            yaml_n_wise_dct = self.yaml_full_dct.copy()
            yaml_key_index_dct = OrderedDict()
            for index, val in self.yaml_full_dct:
                yaml_key_index_dct[val] = index
            return yaml_n_wise_dct, yaml_key_index_dct
        else:
            print('Enter a proper n-wise arguement !!!!')
            exit(1)

    def compute_length_item(self):
        # Creating a dictionery where key is the item name and value is its length
        self.yaml_keys_len = OrderedDict()
        for item in self.yaml_full_dct:
            self.yaml_keys_len[item] = len(self.yaml_full_dct[item])

    def create_n_wise_dct(self, n_wise):
        # Creating two dicts i.n-wise dict
        # ii.yaml_key_index_dct  where key is the item name and value is its position in yaml file
        # To Do : Combine this into one dict with key as item name
        temp_len_dct = self.yaml_keys_len.copy()
        yaml_n_wise_dct = {}
        yaml_key_index_dct = OrderedDict()
        counter = 0
        while counter < n_wise:
            field_with_max_len = max(temp_len_dct, key=temp_len_dct.get)
            yaml_n_wise_dct[field_with_max_len] = self.yaml_full_dct[field_with_max_len]
            lst_yaml_full_keys = list(self.yaml_full_dct.keys())

            # Fetching the index of the max length field
            yaml_key_index_dct[field_with_max_len] = lst_yaml_full_keys.index(field_with_max_len)
            del temp_len_dct[field_with_max_len]
            counter += 1
            # yaml_key_index_dct is the dict where key is the field name in n-wise dct and value is its index in original dct
        return yaml_n_wise_dct, yaml_key_index_dct
