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
def est_terminal(token) :
    #les non terminaux dans la grammaire sont en majuscule
    return token.isupper()
    

#début du parseur:
#L'analyseur prend en entrée la phrase (la liste de token) à identifier et la table d'analyse LL 
#Pour réaliser l'analyse on crée une pile qui à l'initialisation contient l'axiome de la grammaire 
#L'analyseur donne en sortie la liste des règles qui permettent de construire la phrase. Avec cette liste on va créer l'AST

def parse(list_tokens,lexical_table) :
    pile = [] #on crée la pile
    pile.append("F") #on empile l'axiome de la grammaire
    
    token_lu = list_tokens[0]
    sommet_pile = pile[-1] 
    succes = False 
    erreur = False
    ind = 0 #indice de la liste de token

    while not(succes or erreur) :
        
        sommet_pile = pile[-1]
        token_lu = list_tokens[ind]
        
        if (not est_terminal(sommet_pile)) :
            
            if lexical_table[sommet_pile][token_lu]: #Si la table contient une règle pour le couple (sommet_pile,token_lu)
                pile.pop() #on dépile le sommet de la pile
                regle = lexical_table[sommet_pile][token_lu] #on récupère la règle correspondante, qui sera une liste de token
                regle.reverse()
                for i in regle:
                    pile.append(i)
                #for i in range(len(regle)-1,-1,-1) : #on empile les tokens de la règle dans l'ordre inverse
                    #pile.append(regle[i])
            else :
                erreur = True #si la table ne contient pas de règle pour le couple (sommet_pile,token_lu) alors on a une erreur
                
        else : #si x le sommet de la pile est un terminal
            if (sommet_pile == "eof") : #la pile est vide
                if (token_lu == "eof") :
                    succes = True #si on est à la fin de la liste de token et que le sommet de la pile est eof alors on a réussi
                else :
                    erreur = True
                
            else: #la pile n'est pas vide
                if (sommet_pile == token_lu) :
                    pile.pop()
                    ind += 1 #On lit le token suivant
                else :
                    erreur = True                    
  
#il faut traiter les erreurs correctement et construire les fonctions nécessaires.
#Attention à verifier dans token_lu qu'on copare bien la valeur du token!!!!
    
   

            





