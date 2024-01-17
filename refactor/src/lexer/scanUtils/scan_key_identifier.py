import sys

from errorHandling.lexical_error import RemWithoutSpaceException, ForbiddenAsciiException


def scan_key_identifier(source_code: str, position: int, line: int, kw: list) -> "tuple[int, str, int]":
    """
    Scan an entire identifier if we saw one in the source code and raise error if rem func if incorrectly used
    :param source_code: the string of source code
    :param position: the current position in the lexing
    :param line: the current line that we are parsing
    :param kw: the list of language key word
    :return: the place in the lexical table, the value in the lexical table and the position we are in source_code
    """
    string = source_code[position]
    position += 1

    # Faut voir si on a Ada.Text_IO

    while position < len(source_code) and (source_code[position].isalnum() or source_code[position] == "_"):
        # try if we have a non-printable character in the code
        try:
            if ord(source_code[position]) not in range(32, 127) and source_code[position] != "\n":
                raise ForbiddenAsciiException()
        except ForbiddenAsciiException as e:
            print(e, line)
            sys.exit(1)

        # we need to check that rem is followed by ' ', if not we will to retrieve a syntax error in the analysis
        try:
            if string == "rem" and (source_code[position].isnumeric()):
                raise RemWithoutSpaceException()
        except RemWithoutSpaceException as e:
            print(e, line)
            sys.exit(1)

        if string == "Ad" and source_code[position] == "a" and position + 1 < len(source_code) and source_code[position + 1] == ".":
            string += source_code[position]
            string += source_code[position + 1]

            position += 2

            continue

        string += source_code[position]

        position += 1

    return 0 if string.lower() in kw else 3, string.lower(), position
