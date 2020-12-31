class BaseDeleteBookError(Exception):
    def __init__(self, disc):
        self.message = disc
        super().__init__(self.message)


class NonExistentBook(BaseDeleteBookError):
    pass
class NoIssuance(BaseDeleteBookError):
    pass

class BookIsNotAvailable(BaseDeleteBookError):
    pass