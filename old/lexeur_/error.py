# list of all the error handled by the lexical analysis

class RemWithoutSpace(Exception):
    """
        Raised when a rem operator is used without space after him
    """
    pass


class ForbiddenAscii(Exception):
    """
        Raised when a non-printable ascii character is used
    """
    pass


class IdenfierBeginWithNumber(Exception):
    """
        Raised when a identifier begin by a number
    """
    pass
