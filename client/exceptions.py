class HedoraException(Exception):
    pass


class HedoraParameterException(ArkException):
    pass


class HedoraHTTPException(ArkException):

    def __init__(self, *args, **kwargs):
        self.response = kwargs.pop('response', None)
        super().__init__(*args, **kwargs)
