from Exceptions_Demo.custom_exceptions import CustomException, CustomIndexError


class CustomExceptionsDemo:
    def __init__(self):
        print('Inside CustomExceptionsDemo')

    def call_exception(self):
        raise CustomException('Custom Exception Thrown')

    def call_Error(self):
        raise CustomIndexError('Custom Error Thrown')


if __name__ == '__main__':
    obj1 = CustomExceptionsDemo()
    # obj1.call_exception()
    try:
        # obj1.call_exception()
        obj1.call_Error()
    except Exception as e:
        print(e)
