import yaml
import ast
import yamlordereddictloader

Brand = 'Brand-X'
Platform = ''
Version = 3


def read_yaml():
    Platform = ''
    with open('conditions.yaml', 'r') as file_handle:
        cfg = yaml.load(file_handle, Loader=yamlordereddictloader.Loader)
        return cfg['Conditions']


c1 = read_yaml()
# exec(c1)

for condn in c1:
    print(condn)
    exec(condn)
    print(Version)
