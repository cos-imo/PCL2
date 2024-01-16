class ForbiddenAsciiException(Exception):
    """
        Raised when a non-printable ascii character is used
    """
    def __init__(self, message='Use of a non printable ACSII at line :'):
        super(ForbiddenAsciiException, self).__init__(message)


class RemWithoutSpaceException(Exception):
    """
        Raised when a rem operator is used without space after him
    """
    def __init__(self, message="You didn't leave a space after rem usage at line :"):
        super(RemWithoutSpaceException, self).__init__(message)


class IdentifierBeginWithNumberException(Exception):
    """
        Raised when a identifier begin by a number
    """
    def __init__(self, message='You begin an identifier with a number at line :'):
        super(IdentifierBeginWithNumberException, self).__init__(message)
