import unittest
import mock


class Car:
    def __private(self):
        return 1

    def no_private(self):
        return self.__private()


class CarTest(unittest.TestCase):

    # def test_exception_raises(self):
    #     c = Car()
    #     with self.assertRaises(AttributeError):
    #         c.__private()
    #
    # def test_car_works(self):
    #     c = Car()
    #     self.assertEqual(c.no_private(), 1)

    def test_mock_private(self):
        c = Car()
        with mock.patch.object(c, '_Car__private') as method:
            c.no_private()
            method.return_value = 4
            val = c.no_private()
            assert(4 == val)
            # method.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
