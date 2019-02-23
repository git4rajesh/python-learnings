from Design_Patterns.Behavioural.Command.light_commands import *
from Design_Patterns.Behavioural.Command.television_commands import *
from Design_Patterns.Behavioural.Command.remote_control import RemoteControl
from Design_Patterns.Behavioural.Command.lights import Lights
from Design_Patterns.Behavioural.Command.television import Television


class Client:
    @staticmethod
    def run(command):
        remote_obj = RemoteControl(command)
        remote_obj.press()

    @staticmethod
    def run_undo(command):
        remote_obj = RemoteControl(command)
        remote_obj.unpress()


if __name__ == '__main__':
    lights_frontdesk = Lights()
    lights_reception = Lights()
    lights_on_cmd = LightsOnCommand()
    lights_off_cmd = LightsOffCommand()

    Client.run(lights_on_cmd)
    Client.run(lights_off_cmd)

    tv = Television()
    tv_on_cmd = TvOnCommand(tv)
    tv_off_cmd = TvOffCommand(tv)

    Client.run(tv_on_cmd)
    Client.run(tv_off_cmd)

    tv_vol_cmd = TvVolumeCommand(tv)
    Client.run(tv_vol_cmd)
    Client.run_undo(tv_vol_cmd)
