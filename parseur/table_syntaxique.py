# Création de la table syntaxique

# lexical_table = {
#         0: ["access", "and", "begin", "else", "elsif", "end", "false", "for", "function", "if", "in", "is", "loop",
#             "new", "not", "null", "or", "out", "procedure", "record", "rem", "return", "reverse", "then", "true",
#             "type", "use", "while", "with", "character", "integer"],
#         1: ["+", "-", "*", "/", "<", ">", "<=", ">=", "=", "/=", "=>", ".", ":=", ".."],
#         2: ["!", chr(34), "#", "$", "%", "&", "'", "(", ")", ",", ":", ";", "?", "@", "[", chr(92), "]", "^", "_", "`",
#             "{", "|", "}", "~"],
#         3: [], 4: [], 5: []}


#############################################################
# F -> with adatext_io; use adatext_io; procedure ID is DE begin ISP end IDB ; eof.
# D -> type ID D' | IDPV : T EXEGB ; | procedure ID PSB is DE begin ISP end IDB | function ID PSB return T is DE begin ISP end IDB.
# D' -> ; | is D''.
# D'' -> access ID ; | record CP end record;.
# C -> IDVP : T ;.
# T-> ID | access ID.
# PS -> (PPVP).
# P -> IDVP : MB T.
# M -> in M'.
# M' -> out | .
# EX -> OPE.
# IS -> EX IS' | return EXB ; | begin ISP end; | while EX loop ISP end loop; | if EX then ISP ELSIFE ELSEB end if; | for ID in reverse? EX _ EX loop ISP end loop;.
# IS' -> :eg EX | ; .
# O -> eg | dif | inf | sup | infeg | supeg | + | moins | * | / | rem | and O' | or O''.
# O' -> then |.
# O'' -> else |.
# OPE -> OPE1 OPE'.
# OPE' -> ORELS OPE1 OPE' |.
# OPE1 -> OPE2 OPE1'.
# OPE1' -> AND OPE2 OPE1' |.
# OPE2 -> OPE3 OPE2'.
# OPE2' -> not OPE3 OPE2' |.
# OPE3 -> OPE4 OPE3'.
# OPE3' -> EG OPE4 OPE3' |.
# OPE4 -> OPE5 OPE4'.
# OPE4' -> ORDRE OPE5 OPE4' |.
# OPE5 -> OPE6 OPE5'.
# OPE5' -> ADD OPE6 OPE5' |.
# OPE6 -> OPE7 OPE6'.
# OPE6' -> MULT OPE7 OPE6' |.
# OPE7 -> moinsun OPE8 | OPE8.
# OPE8 -> EX' OPE8'.
# OPE8' -> pt ID OPE8' |.
# EX' -> EN | CA | true | false | null | (EX) | ID EX'' | new ID | character'val (EX).
# EX'' -> ( EXVP ) | .
# ORELS -> or ORELS'.
# ORELS' -> else |.
# AND -> and AND'.
# AND' -> then |.
# EG -> eg | dif.
# ORDRE -> inf | infeg | sup | supeg.
# ADD -> + | moins.
# MULT -> * | / | rem.
# CP -> c CP'.
# CP' -> CP | .
# ISP -> IS ISP'.
# ISP'-> ISP | .
# IDVP -> ID IDVP'.
# IDVP' -> v IDVP | .
# EXVP -> EX EXVP'.
# EXVP' -> v EXVP | .
# PPVP -> P PPVP v .
# PPVP' -> v PPVP | .
# PSB -> PS |.
# IDB -> ID |.
# MB -> M |.
# EXB -> EX |.
# ELSEB -> else ISP |.
# DE -> D DE |.
# ELSIFE -> elsif EX then ISP ELSIFE |.
# EXEGB -> :eg EX |.
# ID -> id.
# EN -> en.
# C -> c.
# CA -> ca .
#############################################################

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
