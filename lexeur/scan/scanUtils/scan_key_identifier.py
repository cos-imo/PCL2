def scan_key_identifier(source_code: str, position: int, mc: list) -> tuple[int, str, int]:
    string = source_code[position]
    position += 1

    while position < len(source_code) and (source_code[position].isalnum() or source_code[position] == "_"):  # we need to check that rem is followed by ' ', if not we will to retrieve a syntax error in the analysis
        if string == "rem" and (source_code[position].isnumeric()):
            return 5, string, position
        string += source_code[position]
        position += 1

    return 0 if string in mc else 3, string.lower(), position
