class Student(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_string(cls, name_str):
        first_name, last_name = map(str, name_str.split(' '))
        student = cls(first_name, last_name)
        return student

    @classmethod
    def from_json(cls, json_obj):
        # parse json...
        first_name, last_name = json_obj.f_name, json_obj.l_name
        student = cls(first_name, last_name)
        return student

    @classmethod
    def from_pickle(cls, pickle_file):
        # load pickle file...
        first_name, last_name = pickle_file
        student = cls(first_name, last_name)
        return student