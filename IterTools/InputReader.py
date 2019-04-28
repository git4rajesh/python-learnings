import yaml
import yamlordereddictloader


class InputReader:
    def __init__(self, file_name):
        with open(file_name, 'r') as file_handle:
            self.cfg = yaml.load(file_handle, Loader=yamlordereddictloader.Loader)
            self.len = len(self.cfg)
            print(self.cfg)
            print(self.len)

    def get_fields(self, n_wise):
        temp_store = {}
        if n_wise < self.len:
            for index, item in enumerate(self.cfg):
                if index == n_wise:
                    return temp_store
                temp_store[item] = self.cfg[item]

        elif n_wise == self.len:
                temp_store = self.cfg.copy()
                return temp_store
        else:
            print('Enter a proper n-wise arguement')


if __name__ == '__main__':
    obj = InputReader('pict_input.yml')
    my_dct = obj.get_fields(2)
    print(my_dct)
