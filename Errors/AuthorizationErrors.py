

class PasswordError(Exception):
    def __init__(self, disc):
        self.message = disc
        super().__init__(self.message)


class LoginError(Exception):
    def __init__(self, disc):
        self.message = disc
        super().__init__(self.message)

class LoginFormatError(Exception):
    def __init__(self, disc):
        self.message = disc
        super().__init__(self.message)



