from copy import deepcopy

#Fichier contenant les controles sémantiques à faire lors de la fabrication de la TDS


#Fonctions pour la TDS
def getBloc(tds, pile):
    current_node = tds
    for element in pile:
        current_node = current_node[element]
    return current_node

def getVar(tds, pile, variable):
    current_node = getBloc(tds, pile)
    if variable in current_node:
        return True
    else:
        return False
    
def getValue(tds, pile, variable):
    current_node = getBloc(tds, pile)
    return current_node[variable].value

def getParams(tds, pile, fonction):
    current_node = getBloc(tds, pile)
    return current_node[fonction].params

#Controls sémantiques pour les variables

#Controle de l'imbrication des variables 
#(si la variable a été déclarée dans le bloc courant ou dans un bloc parent avant d'être initialisée)
# Retourne Vrai si la variable a déjà été déclarée dans un bloc
def variableImbricationControle(pile_originale, tds, variable):
    pile = deepcopy(pile_originale)
    while (pile and not(getVar(tds, pile, variable))) :
        pile.pop()
    return (pile!=[])

#Controle de l'affectation des variables 
#(si la variable a été initialisée dans le bloc courant ou dans un bloc parent avant d'être utilisée)
def variableAffectationControle(pile_originale, tds, variable):
    pile = deepcopy(pile_originale)
    while (pile) :
        if getVar(tds, pile, variable) and getValue(tds, pile, variable) != None:
            return True
        else :
            pile.pop()
    return False

#Controle du type de la variable
#pour l'instant on ne peut pas le faire, d'ailleurs on le fera peut être dans le controle de l'imbrication ?



#Controls sémantiques pour les fonctions"

#Controle de l'imbrication des fonctions
#(si la fonction a été déclarée dans le bloc courant ou dans un bloc parent avant d'être utilisée)
def fonctionImbricationControle(pile_originale, tds, fonction):
    pile = deepcopy(pile_originale)
    while (pile and not(getVar(tds, pile, fonction))) :
        pile.pop()
    return (pile!=[])

#Controle de l'affectation des fonctions
#(si la fonction a été initialisée dans le bloc courant ou dans un bloc parent avant d'être utilisée)
def fonctionAffectationControle(pile_originale, tds, fonction):
    pile = deepcopy(pile_originale)
    while (pile) :
        if getVar(tds, pile, fonction) and getValue(tds, pile, fonction) != None:
            return True
        else :
            pile.pop()
    return False

#Controle du nombre de paramètres lors de l'appel à une fonction
def fonctionParamControle(pile_originale, tds, fonction, params):
    pile = deepcopy(pile_originale)
    while (pile) :
        if getVar(tds, pile, fonction) and len(getParams(tds, pile, fonction)) == len(params):
            #on vérifie que le nombre de paramètres est le même
            #on pourra ajouter ici le controle des types des paramètres
            return True
        else :
            pile.pop()
    return False


#Vérification supplémentaire pour la grammaire
#on vérifie que expr.ident a bien un ident et pas une expr quelconque 
def accessControle(access):
    if access[1] == "ident": #on vérifie que le deuxième élément est bien un ident 
        return True
    else:
        return False
    
#Vérification spécifique en Ada
    
    
