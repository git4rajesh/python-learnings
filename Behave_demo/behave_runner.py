import os
import sys
from overloading import overload

from behave.configuration import Configuration
from behave.runner import Runner

dir_parent = os.path.join(os.path.dirname(__file__))
sys.path.extend([dir_parent])


class BehaveRunner:
    @overload
    def __init__(self):
        work_dir = dir_parent
        self.config = self.get_config(work_dir)

    @overload
    def __init__(self, dir_feature):
        work_dir = self.get_working_dir(dir_feature)
        self.config = self.get_config(work_dir)

    @overload
    def __init__(self, dir_feature, file_feature):
        work_dir = self.get_working_dir(dir_feature, file_feature)
        self.config = self.get_config(work_dir)

    @staticmethod
    def get_working_dir(dir_feature, file_feature):
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
    len_args = len(sys.argv)

    if len_args == 1:
        client_obj = BehaveRunner()
    elif len_args == 2:
        dir_feature = sys.argv[1]
        client_obj = BehaveRunner(dir_feature)
    else:
        dir_feature = sys.argv[1]
        file_feature = sys.argv[2]
        client_obj = BehaveRunner(dir_feature, file_feature)

    client_obj.run()
