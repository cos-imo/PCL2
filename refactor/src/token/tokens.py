"""
Contain the token classes
:class Token: Represent the token instance produced by the lexer
:class TokenKind: Represent the existing kind of token in the grammar
"""


class TokenKind:
    """Class representing the various knoww kinds of tokens """
    def __init__(self, text_repr="", kinds=[]):
        """Initialize a new Tokenkind and add it to kinds"""
        self.text_repr = text_repr
        kinds.append(self)
        kinds.sort(key=lambda kind: -len(kind.text_repr))

    def __str__(self):
        """Return the represantation of this token kind"""
        return self.text_repr


class Token:
    """
    Single unit element of the input as produced by the tokenizer
    content - additional content about a token:
        for number -> store the number value
        for identifier -> store the identifier name
    repr - string rep of the token
    r (Range) - range of positions that the token covert
    """
    def __init__(self, kind, content="", repr="", r=None):
        """initialize this token"""
        self.kind = kind

        self.content = content if content else str(self.kind)
        self.repr = repr
        self.r = r

    def __repr__(self):
        return self.content

    def __str__(self):
        """Return the token content"""
        return self.repr if self.repr else self.content
