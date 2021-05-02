class MirrorException(Exception):
    pass


class MirrorParameterException(ArkException):
    pass


class MirrorHTTPException(ArkException):

    def __init__(self, *args, **kwargs):
        self.response = kwargs.pop('response', None)
        super().__init__(*args, **kwargs)
