## Import libraries

## UserError Class - Base for extension into additional errors
class UserError(Exception):
    def __init__(self, message):
        self.message = message

class UserNotFoundError(UserError):
    """
    UserNotFoundError placeholder
    """
    pass

class UserAlreadyRegisteredError(UserError):
    """
    UserAlreadyRegisteredError placeholder
    """
    pass

class InvalidEmailError(UserError):
    """
    InvalidEmailError placeholder
    """
    pass

class IncorrectPasswordError(UserError):
    """
    IncorrectPasswordError placeholder
    """
    pass