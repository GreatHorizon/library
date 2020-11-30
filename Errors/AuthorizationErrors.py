

class AuthorizationError(Exception):
    def __init__(self, disc):
        self.message = disc
        super().__init__(self.message)

class LoginFormatError(Exception):
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