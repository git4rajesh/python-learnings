def check_authorization(f):
    def wrapper(*args):
        print(args[0].url)
        return f(*args)

    return wrapper


class Client:
    def __init__(self, url):
        self.url = url

    @check_authorization
    def get(self):
        print('get')


if __name__ == '__main__':
    client_obj = Client('www.gmail.com')
    client_obj.get()
