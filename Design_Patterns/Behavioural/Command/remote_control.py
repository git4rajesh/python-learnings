# This is the invoker class

class RemoteControl:
    def __init__(self, command):
        self.command = command

    def press(self):
        self.command.execute()

    def unpress(self):
        self.command.unexecute()
