# Création de la table syntaxique

# lexical_table = {
#         0: ["access", "and", "begin", "else", "elsif", "end", "false", "for", "function", "if", "in", "is", "loop",
#             "new", "not", "null", "or", "out", "procedure", "record", "rem", "return", "reverse", "then", "true",
#             "type", "use", "while", "with", "character", "integer"],
#         1: ["+", "-", "*", "/", "<", ">", "<=", ">=", "=", "/=", "=>", ".", ":=", ".."],
#         2: ["!", chr(34), "#", "$", "%", "&", "'", "(", ")", ",", ":", ";", "?", "@", "[", chr(92), "]", "^", "_", "`",
#             "{", "|", "}", "~"],
#         3: [], 4: [], 5: []}

table_syntaxique = {
    'F': {
        # Keywords
        'access': 'error',
        'and': 'error',
        'begin': 'error',
        "else": 'error',
        "elsif": 'error',
        "end": 'error',
        "false": 'error',
        "for": 'error',
        "function": 'error',
        "if": 'error',
        "in": 'error',
        "is": 'error',
        "loop": 'error',
        "new": 'error',
        "not": 'error',
        "null": 'error',
        "or": 'error',
        "out": 'error',
        "procedure": 'error',
        "record": 'error',
        "rem": 'error',
        "return": 'error',
        "reverse": 'error',
        "then": 'error',
        "true": 'error',
        "type": 'error',
        "use": 'error',
        "while": 'error',
        "with": 'error',
        "character": 'error',
        "integer": 'error',
        # Operator
        "+": 'error',
        "-": 'error',
        "*": 'error',
        "/": 'error',
        "<": 'error',
        ">": 'error',
        "<=": 'error',
        ">=": 'error',
        "=": 'error',
        "/=": 'error',
        "=>": 'error',
        ".": 'error',
        ":=": 'error',
        "..": 'error',
        # Syntax operator
        "!": 'error',
        chr(34): 'error',
        "#": 'error',"$": 'error',
        "%": 'error',"&": 'error',
        "'": 'error',
        "(": 'error',
        ")": 'error',
        ",": 'error',
        ":": 'error',
        ";": 'error',
        "?": 'error',
        "@": 'error',
        "[": 'error',
        chr(92): 'error',
        "]": 'error',
        "^": 'error',
        "_": 'error',
        "`": 'error',
        "{": 'error',
        "|": 'error',
        "}": 'error',
        "~": 'error',
        # Identifier
        "3": 'error',
        # Constant number
        "4": 'error'
    },

    'G': {
        # Keywords
        'access': 'error',
        'and': 'error',
        'begin': 'error',
        "else": 'error',
        "elsif": 'error',
        "end": 'error',
        "false": 'error',
        "for": 'error',
        "function": 'error',
        "if": 'error',
        "in": 'error',
        "is": 'error',
        "loop": 'error',
        "new": 'error',
        "not": 'error',
        "null": 'error',
        "or": 'error',
        "out": 'error',
        "procedure": 'error',
        "record": 'error',
        "rem": 'error',
        "return": 'error',
        "reverse": 'error',
        "then": 'error',
        "true": 'error',
        "type": 'error',
        "use": 'error',
        "while": 'error',
        "with": 'error',
        "character": 'error',
        "integer": 'error',
        # Operator
        "+": 'error',
        "-": 'error',
        "*": 'error',
        "/": 'error',
        "<": 'error',
        ">": 'error',
        "<=": 'error',
        ">=": 'error',
        "=": 'error',
        "/=": 'error',
        "=>": 'error',
        ".": 'error',
        ":=": 'error',
        "..": 'error',
        # Syntax operator
        "!": 'error',
        chr(34): 'error',
        "#": 'error',"$": 'error',
        "%": 'error',"&": 'error',
        "'": 'error',
        "(": 'error',
        ")": 'error',
        ",": 'error',
        ":": 'error',
        ";": 'error',
        "?": 'error',
        "@": 'error',
        "[": 'error',
        chr(92): 'error',
        "]": 'error',
        "^": 'error',
        "_": 'error',
        "`": 'error',
        "{": 'error',
        "|": 'error',
        "}": 'error',
        "~": 'error',
        # Identifier
        "3": 'error',
        # Constant number
        "4": 'error'
    }
}
