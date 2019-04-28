from mocking_in_python.working_classes.car import create_and_drive
from unittest import TestCase, mock

# Mocking a Function
# class test_chevrolet_beat_car(TestCase):
#     @mock.patch("mocking_in_python.working_classes.car.Car.drive")
#     def test_drive_using_mock_method(self, mock_drive):
#         mock_drive.return_value = "Zzzz Break Down!!"
#         noise = create_and_drive()
#         assert (noise == "Zzzz Break Down!!")

# Mocking a class
# class test_new_car_spec(TestCase):
#     @mock.patch("mocking_in_python.working_classes.car.Car")
#     def test_drive_using_mock_class(self, mock_car):
#         mock_car.return_value.drive.return_value = "Fast and Furious!!"
#         noise = create_and_drive()
#         assert (noise == "Fast and Furious!!")

# Issue in blind mocking
# class test_new_car(TestCase):
#     @mock.patch("mocking_in_python.working_classes.car.Car_v2.drive")
#     def test_drive(self, mock_drive):
#         mock_drive.return_value = "Zzzz Break Down!!"
#         noise = create_and_drive()
#         assert (noise == "Zzzz Break Down!!")


# Use Specing -1 for a method

class test_new_car_spec(TestCase):
    @mock.patch("mocking_in_python.working_classes.car.Car_v2.drive")
    def test_drive(self, mock_drive):
        mock_drive.return_value = "Zzzz Break Down!!"
        noise = create_and_drive()
        assert (noise == "Zzzz Break Down!!")


# Use Specing -2 for a class
class test_new_car_spec(TestCase):
    @mock.patch("mocking_in_python.working_classes.car.Car_v2", autospec=True)
    def test_drive(self, mock_car):
        mock_car.return_value.drive.return_value = "Zzzz Break Down!!"
        noise = create_and_drive()
        assert (noise == "Zzzz Break Down!!")


# One nuance to be aware of when speccing using a Class is that any attribute that is created after an object has been created will not be picked by autospec.
# For example, if I were to add an instance attribute to the Car_v3 class like so:


# class test_new_car_spec(TestCase):
#     @mock.patch("mocking_in_python.working_classes.car.Car_v3", autospec=True)
#     def test_drive(self, mock_car):
#         mock_car.return_value.drive.return_value = "Zzzz Break Down!!"
#         noise = create_and_drive()
#         assert (noise == "Zzzz Break Down!!")


# To Make it work

class test_new_car_spec(TestCase):
    @mock.patch("mocking_in_python.working_classes.car.Car_v3", autospec=True)
    def test_drive(self, mock_car):
        mock_car.return_value.drive.return_value = "Zzzz Break Down!!"
        mock_car.return_value.make = 'Chev'
        noise = create_and_drive()
        assert (noise == "Zzzz Break Down!!")