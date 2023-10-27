def scan_key_identifier(source_code: str, position: int, mc: list) -> tuple[int, str, int]:
    string = source_code[position]
    position += 1
    t = 0

    while position < len(source_code) and (source_code[position].isalnum() or source_code[position] == "_"):
        string += source_code[position]
        position += 1

    # we need to check that rem is followed by ' ', if not we will to retreive a syntax error in the analysis
    if string == "rem" and source_code[position] != ' ': return 5, string, position

    return 0 if string in mc else 3, string, position


def scan_operator(source_code: str, position: int, op: list) -> tuple[int, str, int]:
    temp = source_code[position : position + 2]

    if temp[0] in op and temp[1] in op: return 1, temp, position + 2
    else: return 1 if temp[0] in op else 2, temp[0], position + 1


def get_int(source_code: str, position: int) -> tuple[int, int]:
    temp = 0

    while position < len(source_code) and source_code[position].isdigit():
        temp = temp * 10 + int(source_code[position])
        position += 1

    return temp, position

def scan_number(source_code: str, position: int) -> tuple[int, int or float, int]:
    number, position = get_int(source_code, position)

    if position < len(source_code)-1 and source_code[position] == '.' and source_code[position+1].isdigit():
        position += 1
        decimal, position = get_int(source_code, position)
        number += float("0."+str(decimal))

    return 4, number, position


def scan(source_code: str) -> tuple[list, dict]:
    # init the lexical table with 0 as key words, 1 as operator, 2 as syntax operator, 3 as identifier, 4 as constant number, 5 invalid char
    lexical_table = {
        0: ["access", "and", "begin", "else", "elsif", "end", "false", "for", "function", "if", "in", "is", "loop",
            "new", "not", "null", "or", "out", "procedure", "record", "rem", "return", "reverse", "then", "true",
            "type", "use", "while", "with"],
        1: ["+", "-", "*", "/", "<", ">", "<=", ">=", "=", "/=", "=>", "."],
        2: ["!", chr(34), "#", "$", "%", "&", "'", "(", ")", ",", ":", ";", "?", "@", "[",chr(92), "]", "^", "_", "`", "{", "|", "}" ,"~"],
        3: [], 4: [], 5: []}

    token = []
    position, line = 0, 1

    while position < len(source_code):
        actual = source_code[position]

        # try if we have a blank to skip
        if actual == ' ': position += 1; continue
        if actual == '\n': position += 1; line += 1; continue

        # try if we have a non-printable charater in the code
        if ord(actual) in range(0, 10) or ord(actual) in range(11, 33) or (actual) == 127:
            type_, value, position = 5, source_code[position], position + 1
            lexical_table[type_].append((value, line))
            token.append((type_, len(lexical_table[5])))
            continue

        # get rid of commentary line
        if actual == "-" and source_code[position+1] == "-":
            while source_code[position] != "\n": position += 1
            position += 1
            continue

        # check if we have a key word, operator, constant number or ...
        if actual.isalpha(): type_, value, position = scan_key_identifier(source_code, position, lexical_table[0])
        elif actual.isdigit(): type_, value, position = scan_number(source_code, position)
        else: type_, value, position = scan_operator(source_code, position, lexical_table[1])

        # add in the lexical table if necessary
        if type_ == 3 or type_ == 4 and value not in lexical_table[type_]: lexical_table[type_].append(value)
        if type_ == 5: lexical_table[type_].append((value, line))

        # add the new token in the list
        token.append((type_,lexical_table[type_].index(value))) if type_ != 4 else token.append((type_,value))

    return token, lexical_table