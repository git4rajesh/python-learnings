# class Car(object):
#     def drive(self):
#         return "Zooooom"
#
#
# def create_and_drive():
#     new_car = Car()
#     return new_car.drive()


# class Car_v2(object):
#     def drive(self, speed):
#         return "Zooooom - {0}".format(speed)
#
#
# def create_and_drive():
#     new_car = Car_v2()
#     return new_car.drive()


class Car_v3(object):
    def __init__(self, make):
        self.make = make

    def drive(self, speed):
        return "GOGOGOGO - {0}".format(speed)


def create_and_drive():
    new_car = Car_v3("Porsche")
    print(new_car.make)
    return new_car.drive("FAST")

from mocking_in_python.working_classes.car import create_and_drive
print(create_and_drive())
