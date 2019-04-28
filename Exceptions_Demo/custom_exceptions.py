class CustomException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class CustomIndexError(IndexError):
    def __init__(self, *args, **kwargs):
        IndexError.__init__(self, *args, **kwargs)


