"""Utilities for the parser"""

tokens = None


class SymbolTable:
    """Record every declared symbol"""

    def __init__(self):
        self.symbols = []
        self.new_scopes()

    def new_scopes(self):
        self.symbols.append({})

    def end_scopes(self):
        self.symbols.pop()

    def add_symbol(self, identifier, is_typedef):
        self.symbols[-1][identifier.content] = is_typedef

    def is_typedef(self, identifier):
        name = identifier.content

        for table in self.symbols[::-1]:
            if name in table:
                return table[name]

        return False


symbols = SymbolTable()


def token_is(index, kind):
    """Return true if the next token is of the given kind"""
    global tokens
    return len(tokens) > index and tokens[index].kind == kind


def token_in(index, kinds):
    """Return true if the next token is in the given list of kinds"""
    global tokens
    return len(tokens) > index and tokens[index].kind in kinds


def token_range(start, end):
    """Generate a range that encompasses tokens[start] to token[end - 1]"""
    global tokens

    startI = min(start, end - 1, len(tokens) - 1)
    endI = min(end - 1, len(tokens) - 1)

    return tokens[startI].r + tokens[endI].r


def add_range(parse_func):
    """Return a decorated func that tags produced node with a range"""
    global tokens

    def parse_with_range(index, *args):
        startI = index
        node, endI = parse_func(index, *args)
        node.r = token_range(startI, endI)

        return node, endI

    return parse_with_range()
