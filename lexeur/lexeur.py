from scanner import scan
from error import *


def lexical_analysis(code_source: str) -> (tuple[list, dict] or bool):
    token, lexical_table = scan(code_source)

    if lexical_table[5]:
        for pb in lexical_table[5]:
            if pb == "rem":
                raise RemWithoutSpace(pb[1])
            else:
                raise ForbiddenAscii(pb[1], pb[0])

        return False
    else:
        return token, lexical_table
