import os
import sys

print(os.getcwd())
path = os.path.dirname(__file__)
sys.path.extend([path])

from Decorators import Demo

Demo.higher_order_wrapper(incr, 5)