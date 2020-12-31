
class BaseFormatError(Exception):
    def __init__(self, disc):
        self.message = disc
        super().__init__(self.message)


class EmptyFieldError(BaseFormatError):
    pass

class InvalidFormatForDigit(BaseFormatError):
    pass