from .scanUtils import scan_operator, scan_int, scan_key_identifier


def scanner(source_code: str) -> tuple[list, dict]:
    # init the lexical table with 0 as keywords, 1 as operator, 2 as syntax operator, 3 as identifier, 4 as constant number, 5 invalid char
    lexical_table = {
        0: ["access", "and", "begin", "else", "elsif", "end", "false", "for", "function", "if", "in", "is", 
            "loop", "new", "not", "null", "or", "out", "procedure", "record", "rem", "return", "reverse",
            "then", "true", "type", "use", "while", "with", "character", "integer","adatext_io","eof"],
        1: ["+", "-", "*", "/", "<", ">", "<=", ">=", "=", "/=", "=>", ".", ":=", ".."],
        2: ["!", chr(34), "#", "$", "%", "&", "'", "(", ")", ",", ":", ";", "?", "@", "[", chr(92), "]", "^", 
            "_", "`", "{", "|", "}", "~"],
        3: [], 4: [], 5: []}

    token = []
    position, line = 0, 1

    while position < len(source_code):
        actual = source_code[position]

        # try if we have a blank to skip
        if actual == ' ':
            position += 1
            continue
        if actual == '\n':
            position += 1
            line += 1
            continue

        # try if we have a non-printable character in the code
        if ord(actual) not in range(32, 127) and actual != "\n":
            type_, value, position = 5, source_code[position], position + 1
            lexical_table[type_].append((value, line))
            token.append((type_, len(lexical_table[5]), line))
            continue

        # get rid of commentary line
        if actual == "-" and source_code[position + 1] == "-":
            while source_code[position] != "\n":
                position += 1
            position += 1
            line += 1
            continue

        # check if we have a key word, operator, constant number or ...
        if actual.isalpha():
            type_, value, position = scan_key_identifier(source_code, position, lexical_table[0])
        elif actual.isdigit():
            type_, value, position = scan_int(source_code, position)
        else:
            type_, value, position = scan_operator(source_code, position, lexical_table[1])

        # add in the lexical table if necessary
        if (type_ == 3 or type_ == 4) and value not in lexical_table[type_]:
            lexical_table[type_].append(value)
        if type_ == 5:
            lexical_table[type_].append((value, line))

        # add the new token in the list
        token.append((type_, lexical_table[type_].index(value), line)) if (type_ != 4 and type_ != 5) else token.append(
            (type_, value, line)) if type_ != 5 else token.append(
            (type_, lexical_table[type_].index((value, line)), line))

    return token, lexical_table
