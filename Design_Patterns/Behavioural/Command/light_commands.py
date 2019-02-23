from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

    def unexecute(self):
        pass


# There are concrete command classes

class LightsOnCommand(Command):

    def __init__(self, lights):
        self.lights = Lights()

    def execute(self):
        self.lights.lights_on()


class LightsOffCommand(Command):

    def __init__(self, receiver):
        self.lights = receiver

    def execute(self):
        self.lights.lights_off()


