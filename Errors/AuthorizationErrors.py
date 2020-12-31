
class AuthorizationError(Exception):
    def __init__(self, disc):
        self.message = disc
        super().__init__(self.message)


class FormatError(Exception):
    def __init__(self, disc):
        self.message = disc
        super().__init__(self.message)


class AddBookError(Exception):
    def __init__(self, disc):
        self.message = disc
        super().__init__(self.message)

class IncorrectPassword(Exception):
    def __init__(self, disc):
        self.message = disc
        super().__init__(self.message)

class NotEqualsPasswords(Exception):
    def __init__(self, disc):
        self.message = disc
        super().__init__(self.message)

class NonExistentBook(Exception):
    def __init__(self, disc):
        self.message = disc
        super().__init__(self.message)

class NoIssuance(Exception):
    def __init__(self, disc):
        self.message = disc
        super().__init__(self.message)
