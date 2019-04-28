class Workspace:
    def __init__(self):
        self.name = 'My Workspace'
        self.id = 121

    def create(self):
        print('Logic to create workspace')


class Task:
    def __init__(self):
        self.id = 343

    def create(self):
        print('Logic to create Task')

    def __getattr__(self, item):
        fluent_cls = getattr(Fluent, item)
        return fluent_cls()

from Inner_Classes.Fluent import Workspace
from Inner_Classes.Fluent import Task

class Fluent:

    class InnerWorkspace:
        @classmethod
        def ws_init(cls):
            print('workspace...')
            workspace = Workspace()
            return workspace


    class InnerTask:
        @classmethod
        def t_init(cls):
            print('task...')
            task = Task()
            return task



if __name__ == '__main__':
    fluent = Fluent()
    fluent.InnerWorkspace.ws_init().create().fluent.Inn