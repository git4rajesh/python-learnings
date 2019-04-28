import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dir_name', help='Give a dir for the feature', type=str)
parser.add_argument('-f', '--file_name', help='Give feature file name', type=str)

args = parser.parse_args()

if args.file_name:
    print(args.dir_name + '\\' + args.file_name)
else:
    print(args.dir_name)