# list of all the error handled by the lexical analysis

class RemWithoutSpace(Exception):
    """
        Raised when a rem operator is used without space after him

        Attribute:
            -- line
    """
    pass


class ForbiddenAscii(Exception):
    """
        Raised when a non-printable ascii character is used

        Attribute:
            -- line
            -- character
    """
    pass
