#Définition de la structure de l'arbre
class Node:
    def __init__(self, type, children=None, value=None):
        """
        Initialise un nouveau nœud de l'arbre.

        :param type: Type de nœud (par exemple, 'Add', 'Subtract', 'Number', 'Identifier', etc.)
        :param children: Liste des nœuds enfants (sous-arbres).
        :param value: Valeur du nœud (utile pour les feuilles comme les nombres ou les identifiants).
        """
        self.type = type
        self.children = children if children is not None else []
        self.value = value

    def add_child(self, child):
        """
        Ajoute un enfant à ce nœud.

        :param child: Nœud enfant à ajouter.
        """
        self.children.append(child)

    def __repr__(self):
        """
        Représentation textuelle pour le débogage.
        print(node) permet d'afficher l'arbre sous forme de texte.
        """
        return f"Node({self.type}, children={self.children}, value={self.value})"




#Fonction qui permet de dire si une chaines de caractères est un terminal ou non
def est_terminal(element) :
    #Si l'élément de la pile est un tuple alors c'est un terminal ou que c'est "eof" alors c'est un terminal sinon si c'est une string alors c'est un non terminal
    if (type(element) == tuple) :
        return True
    else :
        return False
    


# Fonction qui permet de faire l'analyse syntaxique
def parse(list_tokens,lexical_table, table_ll1) :
    pile = [] 
    pile.append("F") #on empile l'axiome de la grammaire
    token_lu = list_tokens[0]
    sommet_pile = pile[-1] 
    succes = False 
    erreur = False
    ind = 0 #indice de la liste de token
    pile_arbre = [] #pile qui va contenir les noeuds de l'arbre

    while not (succes or erreur) :
        sommet_pile = pile[-1]
        token_lu = list_tokens[ind]
        
        #Cas 1 : si le sommet de la pile est un non terminal    
        if (not est_terminal(sommet_pile)) :
            token_lu_table = token_lu
            
            #Modification particulière pour les identifiants et les nombres où les règles sont de la forme <type_token, 0> et non <type_token, valeur_token>
            if token_lu[0] == 3 or token_lu[0] == 4 : 
                token_lu_table = (token_lu[0], 0, token_lu[2]) 
            
            # Si la table contient une règle pour le couple (sommet_pile,token_lu)
            rule = table_ll1[sommet_pile].get((token_lu_table[0], token_lu_table[1]))
            if rule is not None:
                if rule != ["epsilon"]:
                    pile.pop()  # on dépile le sommet de la pile
                    regleC = rule.copy()
                    regleC.reverse()  # on inverse la liste de token pour pouvoir empiler les tokens dans l'ordre
                    for i in regleC:
                        pile.append(i)
                else:
                    pile.pop()
            else:
                erreur = True  # si la table ne contient pas de règle pour le couple (sommet_pile,token_lu) alors on a une erreur
                print("Erreur : la table ne contient pas de règle pour le couple (sommet_pile,token_lu). Sommet de la pile : ", sommet_pile, " valeur Token lu : ", lexical_table[token_lu[0]][token_lu[1]], " Ligne : ", token_lu[2])
                                
        #Cas 2 : si le sommet de la pile est un terminal (<type_token, valeur_token> donc forme ou "eof")    
        else : 
            if (sommet_pile == (0,32)) : #si le sommet de la pile est eof
                if (token_lu[1] == 32) and (token_lu[0] == 0) :
                    succes = True #si on est à la fin de la liste de token et que le sommet de la pile est eof alors on a réussi
                else :
                    erreur = True
                    print("Erreur : la pile est vide mais la liste de token n'est pas finie. Sommet de la pile : ",sommet_pile," valeur Token lu : ",lexical_table[token_lu[0]][token_lu[1]], " Ligne : ",token_lu[2])
                
            else: #si le sommet de la pile est un terminal autre que eof
                if ((sommet_pile == (3,0) and token_lu[0] == 3) or (sommet_pile == (4,0) and token_lu[0] == 4)) :
                    pile.pop()
                    ind += 1
                elif (sommet_pile[0] == token_lu[0]) and (sommet_pile[1] == token_lu[1]) :
                    pile.pop()
                    ind += 1
                else :
                    erreur = True    
                    print("Erreur : le sommet de la pile et le token lu ne sont pas les mêmes. Sommet de la pile : ",sommet_pile," Token Lu: ", token_lu) 
    if succes :
        print("L'anlayse syntaxique a réussi sans erreur")
        return True
    else :
        print("L'analyse syntaxique a échoué")
        return False              
  
#il faut traiter les erreurs correctement et construire les fonctions nécessaires.
#Attention à verifier dans token_lu qu'on compare bien la valeur du token!!!!
    
   

            





