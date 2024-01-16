def scan_operator(source_code: str, position: int, op: list, token: list) -> "tuple[int, str, int]":
    """
    Scan an operator if we saw one in the source code
    :param source_code: the string source code
    :param position: the current position in the lexing
    :param op: the list of language operator
    :param token: the token list
    :return: the place in the lexical table, the value in the lexical table and the position we are in source_code
    """
    temp = source_code[position: position + 2]

    if (temp[0] in op and temp in op) or temp == ":=":
        return 1, temp, position + 2
    else:
        if source_code[position] == "-":
            if token[-1][0] == 1 or (token[-1][0] == 2 and token[-1][1] in ["(", ",", ":", ";", "[", "^", chr(92)]):
                value = "\-"
            else:
                value = "-"
        else:
            value = temp[0]

        return 1 if temp[0] in op else 2, value, position + 1
