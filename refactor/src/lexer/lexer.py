import sys

from scanUtils.scan_int import scan_int
from scanUtils.scan_key_identifier import scan_key_identifier
from scanUtils.scan_operator import scan_operator
from errorHandling.lexical_error import ForbiddenAsciiException


def lexer(source_code: str) -> "tuple[list, dict]":
    """
    Do the lexing phase of the compiling
    :param source_code: the string of the source code we want to compile
    :return: a list of the token and a dict which is the lexical table of the source code
    """
    # init the lexical table with 0 as keywords, 1 as operator, 2 as syntax operator, 3 as identifier, 4 as constant number, 5 invalid char
    lexical_table = {
        0: ["access", "and", "begin", "else", "elsif", "end", "false", "for", "function", "if", "in", "is",
            "loop", "new", "not", "null", "or", "out", "procedure", "record", "rem", "return", "reverse",
            "then", "true", "type", "use", "while", "with", "character", "kteger", "ada.text_io", "eof"],
        1: ["+", "-", "*", "/", "<", ">", "<=", ">=", "=", "/=", "=>", ".", ":=", "..", "\-"],  # binary and unary "-"
        2: ["!", chr(34), "#", "$", "%", "&", "'", "(", ")", ",", ":", ";", "?", "@", "[", chr(92), "]", "^",
            "_", "`", "{", "|", "}", "~"],
        3: [], 4: []}

    token = []
    position, line = 0, 1

    while position < len(source_code):
        current = source_code[position]

        # try if we have a blank to skip
        if current == ' ':
            position += 1
            continue
        if current == '\n':
            position += 1
            line += 1
            continue

        # get rid of commentary line
        if current == "-" and source_code[position + 1] == "-":
            while source_code[position] != "\n":
                position += 1
            position += 1
            line += 1
            continue

        # try if we have a non-printable character in the code
        try:
            if ord(current) not in range(32, 127) and current != "\n":
                raise ForbiddenAsciiException()
        except ForbiddenAsciiException as e:
            print(e, line)
            sys.exit(1)

        # check if we have a key word, operator, constant number or ...
        if current.isalpha():
            type_, value, position = scan_key_identifier(source_code, position, line, lexical_table[0])
        elif current.isdigit():
            type_, value, position = scan_int(source_code, position, line)
        else:
            type_, value, position = scan_operator(source_code, position, lexical_table[1], token)

        # add in the lexical table if necessary
        if (type_ == 3 or type_ == 4) and value not in lexical_table[type_]:
            lexical_table[type_].append(value)

        # add the new token in the list
        token.append((type_, lexical_table[type_].index(value), line)) if (type_ != 4) else token.append(
            (type_, lexical_table[type_].index(value), line))

    return token, lexical_table
