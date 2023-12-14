# Les listes fournies
mes_listes = {
    0: ["access", "and", "begin", "else", "elsif", "end", "false", "for", "function", "if", "in", "is", 
        "loop", "new", "not", "null", "or", "out", "procedure", "record", "rem", "return", "reverse",
        "then", "true", "type", "use", "while", "with", "character'val", "integer","adatext_io","eof"],
    1: ["+", "-", "*", "/", "<", ">", "<=", ">=", "=", "/=", "=>", ".", ":=", ".."],
    2: ["!", chr(34), "#", "$", "%", "&", "'", "(", ")", ",", ":", ";", "?", "@", "[", chr(92), "]", "^", 
        "_", "`", "{", "|", "}", "~"],
    3: [], 4: []
}

# Phrase à découper
phrase = ";"

# Fonction pour découper la phrase
def decouper_phrase(phrase, mes_listes):
    mots = phrase.split()
    resultats = []
    for mot in mots:
        mot_original = mot
        # Vérifie si le mot est en majuscules
        if mot.islower() and mot_original in mes_listes[0]:
            mot = (0, mes_listes[0].index(mot_original))
        elif mot_original in mes_listes[1]:
            mot = (1, mes_listes[1].index(mot_original))
        elif mot_original in mes_listes[2]:
            mot = (2, mes_listes[2].index(mot_original))
        elif mot.isdigit():
            mot = (4, 0)
        resultats.append(mot)
    return resultats

# Découpe la phrase en utilisant les listes fournies
resultat = decouper_phrase(phrase, mes_listes)
print(resultat)
