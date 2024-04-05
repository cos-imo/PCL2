"""Token kind actually recognized"""


from token.tokens import TokenKind


keyword_kinds = []
symbol_kinds = []

identifier = TokenKind()
number = TokenKind()

plus = TokenKind("+", symbol_kinds)
minus = TokenKind("-", symbol_kinds)
star = TokenKind("*", symbol_kinds)
slash = TokenKind("/", symbol_kinds)
mod = TokenKind("rem", symbol_kinds)
equals = TokenKind("=", symbol_kinds)
notequal = TokenKind("/=", symbol_kinds)
bool_and = TokenKind("and", symbol_kinds)
bool_or = TokenKind("or", symbol_kinds)
bool_not = TokenKind("not", symbol_kinds)
lt = TokenKind("<", symbol_kinds)
gt = TokenKind(">", symbol_kinds)
ltoe = TokenKind("<=", symbol_kinds)
gtoe = TokenKind(">=", symbol_kinds)

char_kw = TokenKind("character", keyword_kinds)
int_kw = TokenKind("integer", keyword_kinds)

return_kw = TokenKind("return", keyword_kinds)
if_kw = TokenKind("if", keyword_kinds)
else_kw = TokenKind("else", keyword_kinds)
elsif_kw = TokenKind("elsif", keyword_kinds)
loop_kw = TokenKind("loop", keyword_kinds)
while_kw = TokenKind("while", keyword_kinds)
for_kw = TokenKind("for", keyword_kinds)
end_kw = TokenKind("end", keyword_kinds)
reverse_kw = TokenKind("reverse", keyword_kinds)

