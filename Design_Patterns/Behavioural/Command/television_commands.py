from Design_Patterns.Behavioural.Command.light_commands import Command


# There are concrete command classes

class TvOnCommand(Command):
    def __init__(self, receiver):
        self.tv = receiver

    def execute(self):
        self.tv.tv_on()


class TvOffCommand(Command):
    def __init__(self, receiver):
        self.tv = receiver

    def execute(self):
        self.tv.tv_off()


class TvVolumeCommand(Command):
    def __init__(self, receiver):
        self.tv = receiver

    def execute(self):
        self.tv.increase_volume()

    def unexecute(self):
        self.tv.decrease_volume()

# class TvVolumeDecreaseCommand(Command):
#
#     def __init__(self, receiver):
#         self.tv = receiver
#
#     def execute(self):
#         self.tv.decrease_volume()
