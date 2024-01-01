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
    if (type(element) == tuple) or (element == "eof"):
        return True
    else :
        return False
    

#début du parseur:
#L'analyseur prend en entrée la phrase (la liste de token) à identifier et la table d'analyse LL 
#Pour réaliser l'analyse on crée une pile qui à l'initialisation contient l'axiome de la grammaire 
#L'analyseur donne en sortie la liste des règles qui permettent de construire la phrase. Avec cette liste on va créer l'AST


def parse(list_tokens,lexical_table, table_ll1) :
    pile = [] #on crée la pile
    pile.append("F") #on empile l'axiome de la grammaire
    
    token_lu = list_tokens[0]
    sommet_pile = pile[-1] 
    succes = False 
    erreur = False
    ind = 0 #indice de la liste de token
    pile_arbre = [] #pile qui va contenir les noeuds de l'arbre

    while not(succes or erreur) :
        
        sommet_pile = pile[-1]
        token_lu = list_tokens[ind]
        
        if (not est_terminal(sommet_pile)) :
            print("Token lu : ",token_lu)
            print("Sommet de la pile : ",sommet_pile)
            
            
            if token_lu[0] == 3 : #On s'attend à avoir un identifiant
                token_lu_table = (token_lu[0], 0, token_lu[2]) #On récupère le token lu sous la forme (type_token, valeur_token)
            else :
                token_lu_table = token_lu
                
            if table_ll1[sommet_pile][(token_lu_table[0],token_lu_table[1])]: #Si la table contient une règle pour le couple (sommet_pile,token_lu)
                
                #Oncstruire l'arbre avec les éléments de la règle
                
                
                pile.pop() #on dépile le sommet de la pile
                print("Règle cherchée dans la table : table_ll1 []",sommet_pile,"] [ ",token_lu_table,"]")
                regle = table_ll1[sommet_pile][(token_lu_table[0],token_lu_table[1])] #on récupère la règle correspondante, qui sera une liste de token
                print("Règle : ",regle)
                regle.reverse()
                print("Règle inversée : ",regle)
                for i in regle:
                    print("Ajout de ",i," dans la pile")
                    pile.append(i)
                #for i in range(len(regle)-1,-1,-1) : #on empile les tokens de la règle dans l'ordre inverse
                    #pile.append(regle[i])
            else :
                erreur = True #si la table ne contient pas de règle pour le couple (sommet_pile,token_lu) alors on a une erreur
                print("Erreur : la table ne contient pas de règle pour le couple (sommet_pile,token_lu). Sommet de la pile : ",sommet_pile," valeur Token lu : ",lexical_table[token_lu[0]][token_lu[1]], " Ligne : ",token_lu[2])
                
        else : #si x le sommet de la pile est un terminal, donc les éléments de la pile son des tokens de la forme <type_token, valeur_token> ou "eof"
            if (sommet_pile == "eof") : #la pile n'est plus composé que de eof, c'est la fin
                if (token_lu[1] == "eof") :
                    succes = True #si on est à la fin de la liste de token et que le sommet de la pile est eof alors on a réussi
                else :
                    erreur = True
                    print("Erreur : la pile est vide mais la liste de token n'est pas finie. Sommet de la pile : ",sommet_pile," valeur Token lu : ",lexical_table[token_lu[0]][token_lu[1]], " Ligne : ",token_lu[2])
                
            else: #la pile n'est pas vide, on a donc que des élément sommet_pile de la forme <type_token, valeur_token>
                if sommet_pile == (3,0) and token_lu[0] == 3 :
                    pile.pop()
                    ind += 1
                elif (sommet_pile[0] == token_lu[0]) and (sommet_pile[1] == token_lu[1]) :
                    pile.pop()
                    ind += 1 #On lit le token suivant
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
    
   

            





