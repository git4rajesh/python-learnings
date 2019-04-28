

class Task:
    def __init__(self, name, user):
        self.name = name
        self.id = 101
        self.user = user

    def __str__(self):
        return 'This is task: {} with id: {} for user: {} with uid {}'.format(self.name, self.id, self.user.uname, self.user.uid)


class User:
    def __init__(self, name, id):
        self.uname = name
        self.uid = id

# if __name__ == '__main__':
#     user = User('raj', 'u101')
#     task = Task(user)
#     print(task)

from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage

db = TinyDB('db.json')
TinyDB.DEFAULT_STORAGE = MemoryStorage
user1 = User('raj', 'u101')
task = Task('task1', user1)

db.insert({'task1': task})


