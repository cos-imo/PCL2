#Fonction qui permet de dire si une chaines de caractères est un terminal ou non
def est_terminal(element) :
    #Si l'élément de la pile est un tuple alors c'est un terminal ou que c'est "eof" alors c'est un terminal sinon si c'est une string alors c'est un non terminal
    if (type(element) == tuple) :
        return True
    else :
        return False
    
    
# Fonction auxiliaire pour obtenir les règles attendues
def regles_attendues(sommet_pile, table_ll1):
    regles = table_ll1.get(sommet_pile, {})
    attendu = []
    for (type_token, valeur_token), regle in regles.items():
        attendu.append(f"Type de token: {type_token}, Valeur de token: {valeur_token} -> {regle}")
    return attendu
    
def token_to_str(token, lexical_table):
    token_type, token_value, token_line = token
    token_str = lexical_table[token_type][token_value] if token_type in lexical_table else str(token_value)
    return f"{token_str}"


def highlight_error(token_str):
    RED = '\033[91m'
    END = '\033[0m'
    return f"{RED}{token_str}{END}"


# Fonction qui permet de faire l'analyse syntaxique
def parse(list_tokens, lexical_table, table_ll1):
    pile = []
    pile.append("F")  # on empile l'axiome de la grammaire
    token_lu = list_tokens[0]
    sommet_pile = pile[-1]
    succes = False
    erreur = False
    ind = 0  # indice de la liste de token

    while not (succes or erreur):
        sommet_pile = pile[-1]
        token_lu = list_tokens[ind]

        if not est_terminal(sommet_pile):
            token_lu_table = (token_lu[0], 0, token_lu[2]) if token_lu[0] in [3, 4] else token_lu
            rule = table_ll1[sommet_pile].get((token_lu_table[0], token_lu_table[1]))
            if rule is not None:
                if rule != ["epsilon"]:
                    pile.pop()
                    regleC = rule.copy()
                    regleC.reverse()
                    pile.extend(regleC)
                else:
                    pile.pop()
            else:
                erreur = True
                #Affichage de l'erreur
                token_precedent = list_tokens[ind - 1] if ind > 0 else None
                token_suivant = list_tokens[ind + 1] if ind + 1 < len(list_tokens) else None
                print(f"    Erreur de syntaxe détectée à la ligne {token_lu[2]}:")
                if token_precedent and token_suivant:
                    print(f"        {token_to_str(token_precedent, lexical_table)} {highlight_error(token_to_str(token_lu, lexical_table))} {token_to_str(token_suivant, lexical_table)}\n")
                elif token_precedent:
                    print(f"        {token_to_str(token_precedent, lexical_table)} {highlight_error(token_to_str(token_lu, lexical_table))}\n")
                elif token_suivant:
                    print(f"        {highlight_error(token_to_str(token_lu, lexical_table))} {token_to_str(token_suivant, lexical_table)}\n")
        else:
            if sommet_pile == (0, 32):
                if token_lu[1] == 32 and token_lu[0] == 0:
                    succes = True
                else:
                    erreur = True
                    print(f"    Erreur de fin de fichier inattendue: fin du fichier atteinte mais il reste des éléments dans la pile, Ligne {token_lu[2]}")
            else:
                if (sommet_pile == (3, 0) and token_lu[0] == 3) or (sommet_pile == (4, 0) and token_lu[0] == 4):
                    pile.pop()
                    ind += 1
                elif sommet_pile[0] == token_lu[0] and sommet_pile[1] == token_lu[1]:
                    pile.pop()
                    ind += 1
                else:
                    erreur = True
                    print(f"    Erreur de non-correspondance de token: attendu {sommet_pile}, trouvé {lexical_table[token_lu[0]][token_lu[1]]}, Ligne {token_lu[2]}")

    if succes:
        print("L'analyse syntaxique a réussi sans erreur")
        return True
    else:
        print("L'analyse syntaxique a échoué en raison d'une erreur de syntaxe")
        return False
