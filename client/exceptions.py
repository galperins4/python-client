class HederaException(Exception):
    pass


class HederaParameterException(HedoraException):
    pass


class HederaHTTPException(HedoraException):

    def __init__(self, *args, **kwargs):
        self.response = kwargs.pop('response', None)
        super().__init__(*args, **kwargs)
