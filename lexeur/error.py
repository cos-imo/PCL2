# list of all the error handled by the lexical analysis

class RemWithoutSpace(Exception):
    """
        Raised when a rem operator is used without space after him

        Attribute:
            -- line
    """

    def __int__(self, line: int):
        self.line = line

        self.message = f"You have written a 'rem' operator without leaving a space after it at line {self.line}"
        super().__int__(self.message)


class ForbiddenAscii(Exception):
    """
        Raised when a non-printable ascii character is used

        Attribute:
            -- line
            -- character
    """

    def __int__(self, line: int, character: str):
        self.line = line
        self.char = character

        self.message = f"You have used {self.char}, it is a non printable ascii character. At line {self.line}"
        super().__int__(self.message)
