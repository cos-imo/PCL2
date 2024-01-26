def scan_int(source_code: str, position: int) -> "tuple[int, int, int]":
    temp = 0

    while position < len(source_code) and source_code[position].isdigit():
        temp = temp * 10 + int(source_code[position])
        position += 1

    if position < len(source_code) and source_code[position].isalpha():
        return 5, str(temp), position

    return 4, temp, position
