import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file_names', nargs='*', help='give file name')
args = parser.parse_args()
if args.file_names:
    print('file name is: {}'.format(args.file_names))
else:
    print('No param')