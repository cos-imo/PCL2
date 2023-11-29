from scan import scanner
from error import RemWithoutSpace, IdenfierBeginWithNumber, ForbiddenAscii


def lexical_analysis(code_source: str) -> (tuple[list, dict] or bool):
    token, lexical_table = scanner(code_source)

    if lexical_table[5]:
        for pb in lexical_table[5]:
            if pb[0] == "rem":
                raise RemWithoutSpace(f"You need to put a space after a rem operator at line {pb[1]}")
            elif pb[0].isdigit():
                raise IdenfierBeginWithNumber(f"Your identifier begin with a number at line {pb[1]}")
            else:
                raise ForbiddenAscii(f"You used the forbiden ascii character '{pb[0]}', at line {pb[1]}")
    else:
        return token, lexical_table
