import sys

from errorHandling.lexical_error import IdentifierBeginWithNumberException


def scan_int(source_code: str, position: int, line: int) -> tuple[int, int, int]:
    """
    Scan an entire int if we saw one in the source code and raise error if Integer is followed directly by alpha char
    :param source_code: the string source code
    :param position: the current position in the lexing
    :param line: the current line that we are parsing
    :return: the place in the lexical table, the value in the lexical table and the position we are in source_code
    """
    temp = 0

    while position < len(source_code) and source_code[position].isdigit():
        temp = temp * 10 + int(source_code[position])
        position += 1

    # try if we have an identifier that begin with a number
    try:
        if position < len(source_code) and source_code[position].isalpha():
            raise IdentifierBeginWithNumberException()
    except IdentifierBeginWithNumberException as e:
        print(e, line)
        sys.exit(1)

    return 4, temp, position
