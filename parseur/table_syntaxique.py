# Création de la table syntaxique

# lexical_table = {
#         0: ["access", "and", "begin", "else", "elsif", "end", "false", "for", "function", "if", "in", "is", "loop",
#             "new", "not", "null", "or", "out", "procedure", "record", "rem", "return", "reverse", "then", "true",
#             "type", "use", "while", "with", "character", "integer", "adatext_io", "eof"],
#         1: ["+", "-", "*", "/", "<", ">", "<=", ">=", "=", "/=", "=>", ".", ":=", ".."],
#         2: ["!", chr(34), "#", "$", "%", "&", "'", "(", ")", ",", ":", ";", "?", "@", "[", chr(92), "]", "^", "_", "`",
#             "{", "|", "}", "~"],
#         3: [], 4: [], 5: []}


#############################################################
# F -> with adatext_io ; use adatext_io ; procedure IDENT is DECL_STAR begin INSTR_PLUS end INDENT_BIN ; eof.
# DECL -> type IDENT DECL' | IDENT_VIRG_PLUS : TYPE EXPR_EG_BIN ; | procedure IDENT PARAMS_BIN is DECL_STAR begin INSTR_PLUS end INDENT_BIN ; | function IDENT PARAMS_BIN return TYPE is DECL_STAR begin INSTR_PLUS end INDENT_BIN ; .
# DECL' -> ; | is DECL''.
# DECL'' -> access IDENT ; | record CHAMPS_PLUS end record ;.
# CHAMPS -> IDENT_VIRG_PLUS : TYPE ;.
# TYPE-> IDENT | access IDENT.
# PARAMS -> ( PARAM_POINT_VIRG_PLUS ).
# PARAM -> IDENT_VIRG_PLUS : MODE_BIN TYPE.
# MODE -> in MODE'.
# MODE' -> out | .
# EXPR -> OPE ACCES .
# ACCES -> pt IDENT ACCESS | .
# INSTR -> EXPR INSTR' | return EXPR_BIN ; | begin INSTR_PLUS end ; | while EXPR loop INSTR_PLUS end loop ; | if EXPR then INSTR_PLUS ELSIF_STAR ELSE_BIN end if ; | for IDENT in reverse ? EXPR _ EXPR loop INSTR_PLUS end loop ;.
# INSTR' -> :egal EXPR ; | ; .
# OPE -> OPE1 OPE'.
# OPE' -> ORELS OPE1 OPE' |.
# OPE1 -> OPE2 OPE1'.
# OPE1' -> AND OPE2 OPE1' |.
# OPE2 -> OPE3 OPE2'.
# OPE2' -> not OPE3 OPE2' |.
# OPE3 -> OPE4 OPE3'.
# OPE3' -> EGAL OPE4 OPE3' |.
# OPE4 -> OPE5 OPE4'.
# OPE4' -> ORDRE OPE5 OPE4' |.
# OPE5 -> OPE6 OPE5'.
# OPE5' -> ADD OPE6 OPE5' |.
# OPE6 -> OPE7 OPE6'.
# OPE6' -> MULT OPE7 OPE6' |.
# OPE7 -> moinsun OPE8 | OPE8.
# OPE8 -> EXPR' .
# EXPR' -> ENTIER | true | false | null | ( EXPR ) | IDENT EXPR'' | new IDENT | character'val ( EXPR ).
# EXPR'' -> ( EXPR_VIRG_PLUS ) | .
# ORELS -> or ORELS'.
# ORELS' -> else |.
# AND -> and AND'.
# AND' -> then |.
# EGAL -> egal | dif.
# ORDRE -> inf | infeg | sup | supeg.
# ADD -> + | moins.
# MULT -> * | / | rem.
# CHAMPS_PLUS -> CHAMPS CHAMPS_PLUS'.
# CHAMPS_PLUS' -> CHAMPS_PLUS | .
# INSTR_PLUS -> INSTR INSTR_PLUS'.
# INSTR_PLUS'-> INSTR_PLUS | .
# IDENT_VIRG_PLUS -> IDENT IDENT_VIRG_PLUS'.
# IDENT_VIRG_PLUS' -> v IDENT_VIRG_PLUS | .
# EXPR_VIRG_PLUS -> EXPR EXPR_VIRG_PLUS'.
# EXPR_VIRG_PLUS' -> v EXPR_VIRG_PLUS | .
# PARAM_POINT_VIRG_PLUS -> PARAM PARAM_POINT_VIRG_PLUS' .
# PARAM_POINT_VIRG_PLUS' -> v PARAM_POINT_VIRG_PLUS | .
# PARAMS_BIN -> PARAMS |.
# INDENT_BIN -> IDENT |.
# MODE_BIN -> MODE |.
# EXPR_BIN -> EXPR |.
# ELSE_BIN -> else INSTR_PLUS |.
# DECL_STAR -> DECL DECL_STAR | .
# ELSIF_STAR -> elsif EXPR then INSTR_PLUS ELSIF_STAR |.
# EXPR_EG_BIN -> :egal EXPR |.
# IDENT -> id.
# ENTIER -> en.
#############################################################

table_syntaxique = {
    'F': {
        # Keywords
        # with
        (0,28): [(0, 28), (0, 31), (2, 11), (0, 26), (0, 31), (2, 11), (0, 18), 'IDENT', (0, 11), 'DECL_STAR', (0, 2), 'INSTR_PLUS', (0, 5), 'IDENT_BIN', (2, 11), (0, 32)],
    },
    'DECL': {
        # Keywords
        # function
        (0,8): [(0, 8), 'IDENT', 'PARAMS_BIN', (0, 21), 'TYPE', (0, 11), 'DECL_STAR', (0, 2), 'INSTR_PLUS', (0, 5), 'IDENT_BIN', (2, 11)],
        # procedure
        (0,18): [(0, 18), 'IDENT', 'PARAMS_BIN', (0, 11), 'DECL_STAR', (0, 2), 'INSTR_PLUS', (0, 5), 'IDENT_BIN', (2, 11)],
        # type
        (0,25): [(0, 25), 'IDENT', "DECL'"],
        
        # Identifier

        (3,0): ['IDENT_VIRG_PLUS', (2, 10), 'TYPE', 'EXPR_EG_BIN', (2, 11)],
    },
    "DECL'": {
        # Keywords
        # is
        (0,11): [(0, 11), "DECL''"],

        # Syntax operator
        # ;
        (2,11): [(2, 11)],
    },
    "DECL''": {
        # Keywords
        # access
        (0,0): [(0, 0), 'IDENT', (2, 11)],
        # record        
        (0,19): [(0, 19), 'CHAMPS_PLUS', (0, 5), (0, 19), (2, 11)],
    },
    'CHAMPS': {
        # Identifier
        (3,0): ['IDENT_VIRG_PLUS', (2, 10), 'TYPE', (2, 11)],
    },
    'TYPE': {
        # Keywords
        # access
        (0,0):  [(0, 0), 'IDENT'],

        # Identifier
        (3,0): ['IDENT'],
        
        # Constant number
        
        (4,0): ['error']
    },
    'PARAMS': {
        # Syntax operator
        # (
        (2,7): [(2, 7), 'PARAM_POINT_VIRG_PLUS', (2, 8)],
    },
    'PARAM': {
        # Identifier
        (3,0): ['IDENT_VIRG_PLUS', (2, 10), 'MODE_BIN', 'TYPE'],
    },
    'MODE': {
        # Keywords
        # in
        (0,10): [(0, 10), "MODE'"],
    },
    "MODE'": {
        # Keywords
        # access
        (0,0): [],
        # out
        (0,16): [(0, 17)],
        
        # Identifier
        (3,0): [],
    },
    "EXPR": {
        # Keywords
        # access
        # false
        (0,6): ['OPE', 'ACCES'],
        # new
        (0,13): ['OPE', 'ACCES'],
        # null
        (0,15): ['OPE', 'ACCES'],
        # true
        (0,24): ['OPE', 'ACCES'],
        # character'val
        (0,29): ['OPE', 'ACCES'],

        # Operator
        # -(unaire)
        (1,14): ['OPE', 'ACCES'],

        # Syntax operator
        # (
        (2,7): ['OPE', 'ACCES'],
        
        # Identifier

        (3,0): ['OPE', 'ACCES'],
        
        # Constant number
        
        (4,0): ['OPE', 'ACCES']
    },
    'ACCES': {
        # Keywords
        # loop
        (0,12): [],
        # then
        (0,23): [],

        # Operator
        # .
        (1,11): [[(1, 11), 'IDENT', 'ACCESS']],
        # :=
        (1,12): [],

        # Syntax operator
        # )
        (2,8): [],
        # ,
        (2,9): [],
        # ;
        (2,11): [],
        # _
        (2,18): [],
    },
    'INSTR': {
        # Keywords
        # begin
        (0,2): [(0, 2), 'INSTR_PLUS', (0, 5), (2, 11)],
        # false
        (0,6): ['EXPR', "INSTR'"],
        # for
        (0,7): [(0, 7), 'IDENT', (0, 10), (0, 22), (2, 12), 'EXPR', (2, 18), 'EXPR', (0, 12), 'INSTR_PLUS', (0, 5), (0, 12), (2, 11)],
        # if
        (0,9): [(0, 9), 'EXPR', (0, 23), 'INSTR_PLUS', 'ELSIF_STAR', 'ELSE_BIN', (0, 5), (0, 9), (2, 11)],
        # new
        (0,13): ['EXPR', "INSTR'"],
        # null
        (0,15): ['EXPR', "INSTR'"],
        # return
        (0,21): [(0, 21), 'EXPR_BIN', (2, 11)],
        # true
        (0,24): ['EXPR', "INSTR'"],
        # while
        (0,27): [(0, 27), 'EXPR', (0, 12), 'INSTR_PLUS', (0, 5), (0, 12), (2, 11)],
        # character'val
        (0,29): ['EXPR', "INSTR'"],

        # Operator
        # -(unaire)
        (1,14): ['EXPR', "INSTR'"],

        # Syntax operator
        # (
        (2,7): ['EXPR', "INSTR'"],
        
        # Identifier

        (3,0): ['EXPR', "INSTR'"],
        
        # Constant number
        
        (4,0): ['EXPR', "INSTR'"]
    },
    "INSTR'": {
        # Operator
        # :=
        (1,12): [(1, 12), 'EXPR', (2, 11)],

        # Syntax operator
        # ;
        (2,11): [(2, 11)]
    },
    'OPE': {
        # Keywords
        # false
        (0,6): ['OPE1', "OPE'"],
        # new
        (0,13): ['OPE1', "OPE'"],
        # null
        (0,15): ['OPE1', "OPE'"],
        # true
        (0,24): ['OPE1', "OPE'"],
        # character'val
        (0,29): ['OPE1', "OPE'"],

        # Operator
        # -(unaire)
        (1,14): ['OPE1', "OPE'"],

        # Syntax operator
        # (
        (2,7): ['OPE1', "OPE'"],
        
        # Identifier

        (3,0): ['OPE1', "OPE'"],
        
        # Constant number
        
        (4,0): ['OPE1', "OPE'"]
    },
    "OPE'": {
        # Keywords
        # loop
        (0,12): [],
        # or
        (0,16): ['ORELS', 'OPE1', "OPE'"],
        # then
        (0,23): [],

        # Operator
        # .
        (1,11): [],
        # :=
        (1,12): [],

        # Syntax operator
        # )
        (2,8): [],
        # ,
        (2,9): [],
        # ;
        (2,11): [],
        # _
        (2,18): []
    },
    'OPE1': {
        # Keywords
        # false
        (0,6): ['OPE2', "OPE1'"],
        # new
        (0,13): ['OPE2', "OPE1'"],
        # null
        (0,15): ['OPE2', "OPE1'"],
        # true
        (0,24): ['OPE2', "OPE1'"],
        # character'val
        (0,29): ['OPE2', "OPE1'"],

        # Operator
        # -(unaire)
        (1,14): ['OPE2', "OPE1'"],

        # Syntax operator
        # (
        (2,7): ['OPE2', "OPE1'"],
        
        # Identifier

        (3,0): ['OPE2', "OPE1'"],
        
        # Constant number
        
        (4,0): ['OPE2', "OPE1'"]
    },
    "OPE1'": {
        # Keywords
        # and
        (0,1): ['AND', 'OPE2', "OPE1'"],
        # loop
        (0,12): [],
        # or
        (0,16): [],
        # then
        (0,23): [],

        # Operator
        # .
        (1,11): [],
        # :=
        (1,12): [],

        # Syntax operator
        # )
        (2,8): [],
        # ,
        (2,9): [],
        # ;
        (2,11): [],
        # _
        (2,18): [],
    },
    "OPE2": {
        # Keywords
        # false
        (0,6): ['OPE3', "OPE2'"],
        # new
        (0,13): ['OPE3', "OPE2'"],
        # null
        (0,15): ['OPE3', "OPE2'"],
        # true
        (0,24): ['OPE3', "OPE2'"],
        # character'val
        (0,29): ['OPE3', "OPE2'"],

        # Operator
        # -(unaire)
        (1,14): ['OPE3', "OPE2'"],

        # Syntax operator
        # (
        (2,7): ['OPE3', "OPE2'"],
        
        # Identifier

        (3,0): ['OPE3', "OPE2'"],
        
        # Constant number
        
        (4,0): ['OPE3', "OPE2'"]
    },
    "OPE2'": {
        # Keywords
        # and
        (0,1): [],
        # loop
        (0,12): [],
        # not
        (0,14): [(0, 14), 'OPE3', "OPE2'"],
        # or
        (0,16): [],
        # then
        (0,23): [],

        # Operator
        # .
        (1,11): [],
        # :=
        (1,12): [],

        # Syntax operator
        # )
        (2,8): [],
        # ,
        (2,9): [],
        # ;
        (2,11): [],
        # _
        (2,18): []
    },
    "OPE3": {
        # Keywords
        # false
        (0,6): ['OPE4', "OPE3'"],
        # new
        (0,13): ['OPE4', "OPE3'"],
        # null
        (0,15): ['OPE4', "OPE3'"],
        # true
        (0,24): ['OPE4', "OPE3'"],
        # character'val
        (0,29): ['OPE4', "OPE3'"],

        # Operator
        # -(unaire)
        (1,14):['OPE4', "OPE3'"],

        # Syntax operator
        # (
        (2,7): ['OPE4', "OPE3'"],
        
        # Identifier

        (3,0): ['OPE4', "OPE3'"],
        
        # Constant number
        
        (4,0): ['OPE4', "OPE3'"]
    },
    "OPE3'": {
        # Keywords
        # and
        (0,1): [],
        # loop
        (0,12): [],
        # not
        (0,14): [],
        # or
        (0,16): [],
        # then
        (0,23): [],

        # Operator
        # !=
        (1,8): ['EGAL', 'OPE4', "OPE3'"],
        # =
        (1,9): ['EGAL', 'OPE4', "OPE3'"],
        # .
        (1,11): [],
        # :=
        (1,12): [],

        # Syntax operator
        # )
        (2,8): [],
        # ,
        (2,9): [],
        # ;
        (2,11): [],
        # _
        (2,18): []
    },
    "OPE4": {
        # Keywords
        # false
        (0,6): ['OPE5', "OPE4'"],
        # new
        (0,13): ['OPE5', "OPE4'"],
        # null
        (0,15): ['OPE5', "OPE4'"],
        # true
        (0,24): ['OPE5', "OPE4'"],
        # character'val
        (0,29): ['OPE5', "OPE4'"],

        # Operator
        # -(unaire)
        (1,14):['OPE5', "OPE4'"],

        # Syntax operator
        # (
        (2,7): ['OPE5', "OPE4'"],
        
        # Identifier

        (3,0): ['OPE5', "OPE4'"],
        
        # Constant number
        
        (4,0): ['OPE5', "OPE4'"]
    },
    "OPE4'": {
        # Keywords
        # and
        (0,1): [],
        # loop
        (0,12): [],
        # not
        (0,14): [],
        # or
        (0,16): [],
        # then
        (0,23): [],

        # Operator
        # <
        (1,4): ['ORDRE', 'OPE5', "OPE4'"],
        # >
        (1,5): ['ORDRE', 'OPE5', "OPE4'"],
        # <=
        (1,6): ['ORDRE', 'OPE5', "OPE4'"],
        # >=
        (1,7): ['ORDRE', 'OPE5', "OPE4'"],
        # /=
        (1,8): [],
        # =
        (1,9): [],
        # .
        (1,11): [],
        # :=
        (1,12): [],

        # Syntax operator
        # )
        (2,8): [],
        # ,
        (2,9): [],
        # ;
        (2,11): [],
        # _
        (2,18): []
    },
    "OPE5": {
        # Keywords
        # false
        (0,6): ['OPE6', "OPE5'"],
        # new
        (0,13): ['OPE6', "OPE5'"],
        # null
        (0,15): ['OPE6', "OPE5'"],
        # true
        (0,24): ['OPE6', "OPE5'"],
        # character'val
        (0,29): ['OPE6', "OPE5'"],

        # Operator
        # -(unaire)
        (1,14): ['OPE6', "OPE5'"],

        # Syntax operator
        # (
        (2,7): ['OPE6', "OPE5'"],
        
        # Identifier

        (3,0): ['OPE6', "OPE5'"],
        
        # Constant number
        
        (4,0): ['OPE6', "OPE5'"]
    },
    "OPE5'": {
        # Keywords
        # and
        (0,1): [],
        # loop
        (0,12): [],
        # not
        (0,14): [],
        # or
        (0,16): [],
        # then
        (0,23): [],

        # Operator
        # +
        (1,0): ['ADD', 'OPE6', "OPE5'"],
        # -
        (1,1): ['ADD', 'OPE6', "OPE5'"],
        # <
        (1,4): [],
        # >
        (1,5): [],
        # <=
        (1,6): [],
        # >=
        (1,7): [],
        # /=
        (1,8): [],
        # =
        (1,9): [],
        # .
        (1,11): [],
        # :=
        (1,12): [],

        # Syntax operator
        # )
        (2,8): [],
        # ,
        (2,9): [],
        # ;
        (2,11): [],
        # _
        (2,18): []
    },
    "OPE6": {
        # Keywords
        # false
        (0,6): ['OPE7', "OPE6'"],
        # new
        (0,13): ['OPE7', "OPE6'"],
        # null
        (0,15):  ['OPE7', "OPE6'"],
        # true
        (0,24): ['OPE7', "OPE6'"],
        # character'val
        (0,29):  ['OPE7', "OPE6'"],

        # Operator
        # -(unaire)
        (1,14): ['OPE7', "OPE6'"],

        # Syntax operator
        # (
        (2,7): ['OPE7', "OPE6'"],
        
        # Identifier

        (3,0): ['OPE7', "OPE6'"],
        
        # Constant number
        
        (4,0): ['OPE7', "OPE6'"]
    },
    "OPE6'": {
        # Keywords
        # and
        (0,1): [],
        # loop
        (0,12): [],
        # not
        (0,14): [],
        # or
        (0,16): [],
        # rem
        (0,20): ['MULT', 'OPE7', "OPE6'"],
        # then
        (0,23): [],

        # Operator
        # +
        (1,0): [],
        # -
        (1,1): [],
        # *
        (1,2): ['MULT', 'OPE7', "OPE6'"],
        # /
        (1,3): ['MULT', 'OPE7', "OPE6'"],
        # <
        (1,4): [],
        # >
        (1,5): [],
        # <=
        (1,6): [],
        # >=
        (1,7): [],
        # /=
        (1,8): [],
        # =
        (1,9): [],
        # .
        (1,11): [],
        # :=
        (1,12): [],

        # Syntax operator
        # )
        (2,8): [],
        # ,
        (2,9): [],
        # ;
        (2,11): [],
        # _
        (2,18): []
    },
    "OPE7": {
        # Keywords
        # false
        (0,6): ['OPE8'],
        # new
        (0,13): ['OPE8'],
        # null
        (0,15): ['OPE8'],
        # true
        (0,24): ['OPE8'],
        # character'val
        (0,29): ['OPE8'],

        # Operator
        # -(unaire)
        (1,14): [(1,14),'OPE8'],

        # Syntax operator
        # (
        (2,7): ['OPE8'],
        
        # Identifier

        (3,0):['OPE8'],
        
        # Constant number
        
        (4,0): ['OPE8']
    },
    "OPE8": {
        # Keywords
        # false
        (0,6): ["EXPR'"],
        # new
        (0,13): ["EXPR'"],
        # null
        (0,15): ["EXPR'"],
        # true
        (0,24): ["EXPR'"],
        # character'val
        (0,29): ["EXPR'"],

        # Operator

        # Syntax operator
        # (
        (2,7): ["EXPR'"],
        
        # Identifier

        (3,0): ["EXPR'"],
        
        # Constant number
        
        (4,0): ["EXPR'"],
    },
    "EXPR'": {
        # Keywords
        # false
        (0,6): [(0,6)],
        # new
        (0,13): [(0, 13), 'IDENT'],
        # null
        (0,15): [(0,15)],
        # true
        (0,24): [(0,24)],
        # character'val
        (0,29): [(0, 29), (2, 7), 'EXPR', (2, 8)],

        # Operator

        # Syntax operator
        # (
        (2,7): [(2, 7), 'EXPR', (2, 8)],
        
        # Identifier

        (3,0): ["IDENT", "EXPR''"],
        
        # Constant number
        
        (4,0): ["ENTIER"],
    },
    "EXPR''": {
        # Keywords
        # and
        (0,1): [],
        # loop
        (0,12): [],
        # not
        (0,14): [],
        # or
        (0,16): [],
        # rem
        (0,20): [],
        # then
        (0,23): [],

        # Operator
        # +
        (1,0): [],
        # -
        (1,1): [],
        # *
        (1,2): [],
        # /
        (1,3): [],
        # <
        (1,4): [],
        # >
        (1,5): [],
        # <=
        (1,6): [],
        # >=
        (1,7): [],
        # /=
        (1,8): [],
        # =
        (1,9): [],
        # .
        (1,11): [],
        # :=
        (1,12): [],

        # Syntax operator
        # (
        (2,7): [(2, 7), 'EXPR_VIRG_PLUS', (2, 8)],
        # )
        (2,8): [],
        # ,
        (2,9): [],
        # ;
        (2,11): [],
        # _
        (2,18): []
    },
    'ORELS': {
        # Keywords
        # or
        (0,16): [(0, 16), "ORELS'"]
    },
    "ORELS'": {
        # Keywords
        # else
        (0,3): [(0, 3)],
        # false
        (0,6): [],
        # new
        (0,13): [],
        # null
        (0,15): [],
        # true
        (0,24): [],
        # character'val
        (0,29): [],

        # Operator
        # -(unaire)
        (1,14): [],

        # Syntax operator
        # (
        (2,7): [],
        
        # Identifier

        (3,0):[],
        
        # Constant number
        
        (4,0): []
    },
    'AND': {
        # Keywords
        # and
        (0,1): [(0,1), "AND'"],
    },
    "AND'": {
        # Keywords
        # false
        (0,6): [],
        # new
        (0,13): [],
        # null
        (0,15): [],
        # then
        (0,23): [(0, 23)],
        # true
        (0,24): [],
        # character'val
        (0,29): [],

        # Operator
        # -(unaire)
        (1,14): [],

        # Syntax operator
        # (
        (2,7): [],
        
        # Identifier

        (3,0):[],
        
        # Constant number
        
        (4,0): []
    },
    'EGAL': {
        # Operator
        
        # =
        (1,8): [(1,8)],
        # /=
        (1,9): [(1,9)]
    },
    'ORDRE': {

        # Operator
        # <
        (1,4): [(1,4)],
        # >
        (1,5): [(1,5)],
        # <=
        (1,6): [(1,6)],
        # >=
        (1,7): [(1,7)],
        # =
        (1,8): ['error']
    },
    'ADD': {
        # Operator
        
        # +
        (1,0): [(1,0)],
        # -
        (1,1): [(1,1)]
    },
    'MULT': {
        # Keywords
        #rem
        (0,20): ['error'],

        # Operator
        # *
        (1,2): ['error'],
        # /
        (1,3): ['error'],
    },
    'CHAMPS_PLUS': {
        # Identifier
        (3,0): ['CHAMPS', "CHAMPS_PLUS'"],
    },
    "CHAMPS_PLUS'": {
        # Keywords
        # end
        (0,5): [],
        
        # Identifier
        (3,0): ['CHAMPS_PLUS']
    },
    'INSTR_PLUS': {
        # Keywords
        # begin
        (0,2): ['INSTR', "INSTR_PLUS'"],
        # false
        (0,6): ['INSTR', "INSTR_PLUS'"],
        # for
        (0,7): ['INSTR', "INSTR_PLUS'"],
        # if
        (0,9): ['INSTR', "INSTR_PLUS'"],
        # new
        (0,13): ['INSTR', "INSTR_PLUS'"],
        # null
        (0,15): ['INSTR', "INSTR_PLUS'"],
        # return
        (0,21): ['INSTR', "INSTR_PLUS'"],
        # true
        (0,24): ['INSTR', "INSTR_PLUS'"],
        # while
        (0,27): ['INSTR', "INSTR_PLUS'"],
        # character'val
        (0,29): ['INSTR', "INSTR_PLUS'"],

        # Operator
        # -(unaire)
        (1,14): ['INSTR', "INSTR_PLUS'"],

        # Syntax operator
        # (
        (2,7): ['INSTR', "INSTR_PLUS'"],

        # Identifier
        (3,0): ['INSTR', "INSTR_PLUS'"],
        
        # Constant number
        (4,0): ['INSTR', "INSTR_PLUS'"]
    },
    "INSTR_PLUS'": {
        # Keywords
        # begin
        (0,2): ["INSTR_PLUS"],
        # elsif
        (0,3): [],
        # else
        (0,4): [],
        # end
        (0,5): [],
        # false
        (0,6): ["INSTR_PLUS"],
        # for
        (0,7):["INSTR_PLUS"],
        # if
        (0,9): ["INSTR_PLUS"],
        # new
        (0,13): ["INSTR_PLUS"],
        # null
        (0,15): ["INSTR_PLUS"],
        # return
        (0,21): ["INSTR_PLUS"],
        # true
        (0,24): ["INSTR_PLUS"],
        # while
        (0,27):["INSTR_PLUS"],
        # character'val
        (0,29): ["INSTR_PLUS"],

        # Operator
        # -(unaire)
        (1,14): ["INSTR_PLUS"],

        # Syntax operator
        # (
        (2,7):["INSTR_PLUS"],

        # Identifier
        (3,0): ["INSTR_PLUS"],
        
        # Constant number
        (4,0): ["INSTR_PLUS"]
    },
    'IDENT_VIRG_PLUS': {
        # Identifier
        (3,0): ['IDENT', "IDENT_VIRG_PLUS'"],
    },
    "IDENT_VIRG_PLUS'": {
        # Syntax operator
        # ,
        (2,9): [(2, 9), 'IDENT_VIRG_PLUS'],
        # :
        (2,10): []
    },
    'EXPR_VIRG_PLUS': {
        # Keywords
        # false
        (0,6): ['EXPR', "EXPR_VIRG_PLUS'"],
        # new
        (0,13): ['EXPR', "EXPR_VIRG_PLUS'"],
        # null
        (0,15):['EXPR', "EXPR_VIRG_PLUS'"],
        # true
        (0,24): ['EXPR', "EXPR_VIRG_PLUS'"],
        # character'val
        (0,29): ['EXPR', "EXPR_VIRG_PLUS'"],

        # Operator
        # -(unaire)
        (1,14): ['EXPR', "EXPR_VIRG_PLUS'"],

        # Syntax operator
        # (
        (2,7): ['EXPR', "EXPR_VIRG_PLUS'"],

        # Identifier
        (3,0): ['EXPR', "EXPR_VIRG_PLUS'"],
        
        # Constant number
        (4,0): ['EXPR', "EXPR_VIRG_PLUS'"]
    },
    "EXPR_VIRG_PLUS'": {
        # Syntax operator
        # )
        (2,8): [],
        # ,
        (2,9): [(2, 9), 'EXPR_VIRG_PLUS'],
    },
    'PARAM_POINT_VIRG_PLUS': {
        # Identifier
        (3,0): ['PARAM', "PARAM_POINT_VIRG_PLUS'"],
    },
    "PARAM_POINT_VIRG_PLUS'": {
        # Syntax operator
        # )
        (2,8): [],
        # ,
        (2,9): [(2, 9), 'PARAM_POINT_VIRG_PLUS'],
    },
    'PARAMS_BIN': {
        # Keywords
        # is
        (0,11): [],
        # return
        (0,21): [],

        # Syntax operator
        # (
        (2,7): ['PARAMS']
    },
    'IDENT_BIN': {
        # Syntax operator
        # ;
        (2,11): [],
        
        # Identifier
        (3,0): ['IDENT']
    },
    'MODE_BIN': {
        # Keywords
        # access
        (0,0): [],
        # in
        (0,10): ['MODE'],

        # Identifier
        (3,0): []
    },
    'EXPR_BIN': {
        # Keywords
        # false
        (0,6): ["EXPR"],
        # new
        (0,13): ["EXPR"],
        # null
        (0,15): ["EXPR"],
        # true
        (0,24): ["EXPR"],
        # character'val
        (0,29): ["EXPR"],

        # Operator
        # -(unaire)
        (1,14): ["EXPR"],

        # Syntax operator
        # (
        (2,7): ["EXPR"],
        # ;
        (2,11): [],

        # Identifier
        (3,0): ["EXPR"],
        
        # Constant number
        (4,0): ["EXPR"]
    },
    'ELSE_BIN': {
        # Keywords
        # else
        (0,3): [(0, 3), 'INSTR_PLUS'],
        # end
        (0,5): []
    },
    'DECL_STAR': {
        # Keywords
        # begin
        (0,2): [],
        # function
        (0,8):['DECL', 'DECL_STAR'],
        # procedure
        (0,18): ['DECL', 'DECL_STAR'],
        # type
        (0,25): ['DECL', 'DECL_STAR'],

        # Identifier
        (3,0):['DECL', 'DECL_STAR']
    },
    'ELSIF_STAR': {
        # Keywords
        # else
        (0,3): [],
        # elsif
        (0,4): [(0, 4), 'EXPR', (0, 23), 'INSTR_PLUS', 'ELSIF_STAR'],
        # end
        (0,5): []
    },
    'EXPR_EG_BIN': {
        # Operator
        # :=
        (1,12): [(1, 12), 'EXPR'],

        # Syntax operator
        # ;
        (2,11): []
    },
    'IDENT': {        
        # Constant number
        (4,0): ['error']
    },
    'ENTIER': {
        # Constant number
        (4,0): [(4,0)]
    },
}