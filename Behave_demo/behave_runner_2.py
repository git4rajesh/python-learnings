import os
import sys
from overloading import overload

import argparse


from behave.configuration import Configuration
from behave.runner import Runner

dir_parent = os.path.join(os.path.dirname(__file__))
sys.path.extend([dir_parent])


class BehaveRunner:
    @overload
    def __init__(self):
        print('Inside No arguement constructor')
        work_dir = dir_parent
        self.config = self.get_config(work_dir)

    @overload
    def __init__(self, dir_feature):
        print('Inside One arguement constructor')
        work_dir = self.get_working_dir(dir_feature)
        self.config = self.get_config(work_dir)

    @overload
    def __init__(self, dir_feature, file_feature):
        print('Inside Two arguement constructor')
        work_dir = self.get_working_dir(dir_feature, file_feature)
        self.config = self.get_config(work_dir)

    @staticmethod
    def get_working_dir(dir_feature, file_feature=None):
        dir_complete = dir_parent + '\\' + dir_feature

        if file_feature:
            dir_work = dir_complete + '\\' + file_feature
        else:
            dir_work = dir_complete
        return dir_work

    @staticmethod
    def get_config(work_dir):
        config = Configuration()
        config.paths = [work_dir]
        config.format = ['pretty']
        return config

    def run(self):
        first_runner = Runner(self.config)
        first_runner.run()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file_name', help='Give feature file name', type=str)
    parser.add_argument('-d', '--dir_name', help='Give a dir for the feature', type=str)

    args = parser.parse_args()

    client_obj = None
    if args.file_name and args.dir_name:
        client_obj = BehaveRunner(args.dir_name, args.file_name)
    elif args.dir_name and not args.file_name:
        client_obj = BehaveRunner(args.dir_name)
    elif args.file_name and not args.dir_name:
        print('>>>Usage', 'Provide directory also')
    else:
        client_obj = BehaveRunner()

    print(client_obj)
    # client_obj.run()
