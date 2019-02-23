from Design_Patterns.Structural.Bridge.demo3.animals import Wolves
from Design_Patterns.Structural.Bridge.demo3.animals import Dragons
from Design_Patterns.Structural.Bridge.demo3.got import Targaryens
from Design_Patterns.Structural.Bridge.demo3.got import Starks

wolf_obj = Wolves()
dragon_obj = Dragons()

targ_obj = Targaryens(dragon_obj)
targ_obj.get_details()

stark_obj = Starks(wolf_obj)
stark_obj.get_details()
