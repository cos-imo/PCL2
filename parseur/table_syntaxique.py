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
# F -> with adatext_io; use adatext_io; procedure IDENT is DECL_STAR begin INSTR_PLUS end INDENT_BIN ; eof.
# DECL -> type IDENT DECL' | IDENT_VIRG_PLUS : TYPE EXPR_EG_BIN ; | procedure IDENT PARAMS_BIN is DECL_STAR begin INSTR_PLUS end INDENT_BIN ; | function IDENT PARAMS_BIN return TYPE is DECL_STAR begin INSTR_PLUS end INDENT_BIN ; .
# DECL' -> ; | is DECL''.
# DECL'' -> access IDENT ; | record CHAMPS_PLUS end record;.
# CHAMPS -> IDENT_VIRG_PLUS : TYPE ;.
# TYPE-> IDENT | access IDENT.
# PARAMS -> ( PARAM_POINT_VIRG_PLUS ).
# PARAM -> IDENT_VIRG_PLUS : MODE_BIN TYPE.
# MODE -> in MODE'.
# MODE' -> out | .
# EXPR -> OPE ACCES .
# ACCES -> pt IDENT ACCESS | .
# INSTR -> EXPR INSTR' | return EXPR_BIN ; | begin INSTR_PLUS end; | while EXPR loop INSTR_PLUS end loop; | if EXPR then INSTR_PLUS ELSIFE ELSEB end if; | for IDENT in reverse? EXPR _ EXPR loop INSTR_PLUS end loop ;.
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
# EXPR' -> ENTIER | CARACTERE | true | false | null | ( EXPR ) | IDENT EXPR'' | new IDENT | character'val ( EXPR ).
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
# ELSEB -> else INSTR_PLUS |.
# DECL_STAR -> DECL DECL_STAR | .
# ELSIFE -> elsif EXPR then INSTR_PLUS ELSIFE |.
# EXPR_EG_BIN -> :egal EXPR |.
# IDENT -> id.
# ENTIER -> en.
# CARACTERE -> ca .
#############################################################

table_syntaxique = {
    'F': {
        # Keywords
        # access
        (0,0): ['error'],
        # and
        (0,1): ['error'],
        # begin
        #Ici on renvoie la règle: F -> with adatext_io; use adatext_io; procedure IDENT is DECL_STAR begin INSTR_PLUS end INDENT_BIN ; eof.
        (0,2): [(0,28),(0,31), (2,11,), .....],
        # else
        (0,3): ['error'],
        # elsif
        (0,4): ['error'],
        # end
        (0,5): ['error'],
        # false
        (0,6): ['error'],
        # for
        (0,7): ['error'],
        # function
        (0,8): ['error'],
        # if
        (0,9): ['error'],
        # in
        (0,10): ['error'],
        # is
        (0,11): ['error'],
        # loop
        (0,12): ['error'],
        # new
        (0,13): ['error'],
        # not
        (0,14): ['error'],
        # null
        (0,15): ['error'],
        # out
        (0,16): ['error'],
        # out
        (0,17): ['error'],
        # procedure
        (0,18): ['error'],
        # record        
        (0,19): ['error'],
        #rem
        (0,20): ['error'],
        # return
        (0,21): ['error'],
        #reverse
        (0,22): ['error'],
        # then
        (0,23): ['error'],
        # true
        (0,24): ['error'],
        # type
        (0,24): ['error'],
        # use
        (0,25): ['error'],
        # while
        (0,26): ['error'],
        # with
        (0,27): ['error'],
        # charcater
        (0,28): ['error'],
        # integer
        (0,29): ['error'],

        # Operator
        
        # +
        (1,0): ['error'],
        # -
        (1,1): ['error'],
        # *
        (1,2): ['error'],
        # /
        (1,3): ['error'],
        # <
        (1,4): ['error'],
        # >
        (1,5): ['error'],
        # <=
        (1,6): ['error'],
        # >=
        (1,7): ['error'],
        # =
        (1,8): ['error'],
        # /=
        (1,9): ['error'],
        # =>
        (1,10): ['error'],
        # .
        (1,11): ['error'],
        # :=
        (1,12): ['error'],
        # ..
        (1,13): ['error'],

        # Syntax operator
        
        # !
        (2,0): ['error'],
        # "
        (2,1): ['error'],
        # #
        (2,2): ['error'],
        # $
        (2,3): ['error'],
        # %
        (2,4): ['error'],
        # &
        (2,5): ['error'],
        # '
        (2,6): ['error'],
        # (
        (2,7): ['error'],
        # )
        (2,8): ['error'],
        # ,
        (2,9): ['error'],
        # :
        (2,10): ['error'],
        # ;
        (2,11): ['error'],
        # ?
        (2,12): ['error'],
        # @
        (2,13): ['error'],
        # []
        (2,14): ['error'],
        # \
        (2,15): ['error'],
        # ]
        (2,16): ['error'],
        # ^
        (2,17): ['error'],
        # _
        (2,18): ['error'],
        # `
        (2,19): ['error'],
        # {}
        (2,20): ['error'],
        # |
        (2,21): ['error'],
        # }
        (2,22): ['error'],
        # ~
        (2,23): ['error'],
        
        # Identifier

        (3,0): ['error'],
        
        # Constant number
        
        (4,0): ['error']
    }
}