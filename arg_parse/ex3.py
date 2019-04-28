import argparse
parser = argparse.ArgumentParser()
parser.add_argument("dir_name", help="Give a dir for the feature", type=str)
parser.add_argument("file_name", help="Give feature file name", type=str)
parser.add_argument('--myopt')
args = parser.parse_args()
print(args.dir_name + '\\' + args.file_name)
print(args.myopt)
