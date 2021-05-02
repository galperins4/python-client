class HedoraException(Exception):
    pass


class HedoraParameterException(HedoraException):
    pass


class HedoraHTTPException(HedoraException):

    def __init__(self, *args, **kwargs):
        self.response = kwargs.pop('response', None)
        super().__init__(*args, **kwargs)
