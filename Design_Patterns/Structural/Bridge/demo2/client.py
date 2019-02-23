from Design_Patterns.Structural.Bridge.demo2.colors import Blue
from Design_Patterns.Structural.Bridge.demo2.colors import Red
from Design_Patterns.Structural.Bridge.demo2.shapes import Rect
from Design_Patterns.Structural.Bridge.demo2.shapes import Circle

blue_obj = Blue()
red_obj = Red()

rect_obj = Rect(blue_obj)
rect_obj.get_details()

circle_obj = Circle(red_obj)
circle_obj.get_details()
