def check_authorization(f):
    """
    This is check method doc string
    """
    def wrapper(*args):
        """
        This is wrapper method
        """
        print(args[0].url)
        f(*args)

    return wrapper


class Client:

    def put_method(self):
        print('put')

    @check_authorization
    def get_method(self):
        """
        This is get_method doc string
        """
        self.put_method()
        print('get')









