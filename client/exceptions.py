class HederaException(Exception):
    pass


class HederaParameterException(HederaException):
    pass


class HederaHTTPException(HederaException):

    def __init__(self, *args, **kwargs):
        self.response = kwargs.pop('response', None)
        super().__init__(*args, **kwargs)
