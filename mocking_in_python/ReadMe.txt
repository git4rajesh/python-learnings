https://www.toptal.com/python/an-introduction-to-mocking-in-python
https://www.youtube.com/watch?v=zW0f4ZRYF5M
http://pyvideo.org/pyohio-2013/my-adventures-with-mock.html

1. The Pyramid of Testing.
    - 70% of Unit testing.

2. Great Unit Testing Myths:
    - They are good when the problem is easy.
        A rabbit hole of testing.End up writing unit tests for unit tests as my unit tests are complicated.
    - I spend too much time writing lot of code, so give up on Unit testing.
    - There are just some stuff which we cant Unit Test.

3. Good News.
    - Mocking makes Unit Testing Easy.
    - Development is about making things, while mocking is about faking things

3b. Why Mock?/
    No API yet or Eliminate inter-team dependencies
    Slow or unreliable calls  (DB interactions)
    Collaborators involved in Dependancy injection
    Work offline

4. What are Mocks?

        Test Double
   a. Dummy Object b. Fake Object c. Mock Object d. Test stub e. Test Spy.

        https://adamcod.es/2014/05/15/test-doubles-mock-vs-stub.html
        https://martinfowler.com/bliki/TestDouble.html
        https://testing.googleblog.com/2013/07/testing-on-toilet-know-your-test-doubles.html

        
5.In Python, mocking is accomplished through the unittest.mock module.
The module contains a number of useful classes and functions, the most important of which are the
    a. patch function (as decorator and context manager) and
    b. MagicMock class.


6. Mocking in Python is done by using patch to hijack an API function or object creation call.
When patch intercepts a call, it returns a MagicMock object by default.
By setting properties on the MagicMock object, you can mock the API call to return any value you want or raise an Exception.

7. The overall procedure is as follows:
    Write the test as if you were using real external APIs.
    In the function under test, determine which API calls need to be mocked out; this should be a small number.
    In the test function, patch the API calls.
    Set up the MagicMock object responses.
    Run your test.

8. Patch:
https://blog.fugue.co/2016-02-11-python-mocking-101.html
    import unittest
    from unittest.mock import patch

9. How to Patch:
patch can be used as a decorator to the test function, taking a string naming the function that will be patched as an argument.
In order for patch to locate the function to be patched, it must be specified using its fully qualified name.
Typically patch is used to patch an external API call or any other time- or resource-intensive function call or object creation.
You should only be patching a few callables per test.
Using the patch, decorator will automatically send a positional argument to the function you're decorating (i.e., your test function).
When patching multiple functions, the decorator closest to the function being decorated is called first, so it will create the first positional argument.

    @patch('module.ClassB')
    @patch('module.functionA')
    def test_some_func(self, mock_A, mock_B):

10.By default, these arguments are instances of MagicMock, which is unittest.mock's default mocking object.
You can define the behavior of the patched function by setting attributes on the returned MagicMock instance.

11. MagicMock:
    MagicMock objects provide a simple mocking interface that allows you to set the return value or other behavior of the function or object creation call that you patched.
    This allows you to fully define the behavior of the call and avoid creating real objects, which can be onerous.
    For example, if we're patching a call to requests.get, an HTTP library call, we can define a response to that call that will be returned when the API call is made in the function under test, rather than ensuring that a test server is available to return the desired response.
    The two most important attributes of a MagicMock instance are return_value and side_effect, both of which allow us to define the return behavior of the patched call.

12. return_value:

13. side_effects:
    Side effect functions and iterables.
    multiple calls of the function you're patching are handled correctly
    mock = MagicMock(side_effect=[4, 5, 6])
>>> mock()
4
>>> mock()
5
>>> mock()
6

side_effects using a dictionary:
    >>> values = {'a': 1, 'b': 2, 'c': 3}
    >>> def side_effect(arg):
             return values[arg]

>>> mock.side_effect = side_effect
>>> mock('a'), mock('b'), mock('c')
(1, 2, 3)

13b. side_effect allows you to perform raising an exception when a mock is called:


14. Recap


15. Mocking to Verify behaviour:
    call_count
    checking Parameters?
        - assert_called_once_with(param1)

    PATCH MULTIPLE: We can use it like key-word args.
    @patch.multiple('Class', call_pve = DEFAULT, call_pp =DEFAULT, call_innotas = DEFAULT)
    def test_call_pve(call_pve, call_pp, call_innotas):
15. assert_called_with:

16. unittest.mock.sentinel

	real = ProductionClass()
	real.method = Mock(name="method")
	real.method.return_value = sentinel.some_object
	result = real.method()
	assert result is sentinel.some_object
	sentinel.some_object

17.SPEC:
For example the spec argument configures the mock to take its specification from another object.
Attempting to access attributes or methods on the mock that don’t exist on the spec will fail with an AttributeError.

18. In conclusion, I recommend speccing your mock objects when writing tests but with the understanding
of what it means to do so, as it reduces the risk of a test passing if the code is actually broken.
https://medium.com/python-pandemonium/mocking-has-a-weakness-speccing-removes-it-2d2068a17df8