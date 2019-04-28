Spies
1. A Stub could also be used to maintain state, and make assertions, when a Stub does this it is also known as a Test Spy. 
For example, checking the contents of a parameter, or the total number of times a method is called:
2. Using Python Mock library to spy on internal method calls


You can construct a "spy" using the Mock(spec=obj) constructor which will make the __class__ attribute equal to ClassUnderTest where the Mock(wraps=obj) constructor will not. 
Since in python class methods take the a class instance, the self parameter, as their first parameter, you can call it with a mock as if it were a static method on the class.

class ClassUnderTest(object):
    def lower_1(self):
        print 'lower_1'

    def lower_2(self):
        print 'lower_2'

    def higher(self):
        self.lower_1()
        self.lower_2()



import mock

obj = ClassUnderTest()
spy = mock.Mock(spec=obj)
# test call
ClassUnderTest.higher(spy)

# Assert that lower_1 was called before lower_2
assert spy.mock_calls == [mock.call.lower_1(), mock.call.lower_2()]