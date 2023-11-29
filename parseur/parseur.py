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


#début du parseur:
#L'analyseur prend en entrée la phrase (la liste de token) à identifier et la table d'analyse LL 
#Pour réaliser l'analyse on crée une pile qui à l'initialisation contient l'axiome de la grammaire 
#L'analyseur donne en sortie la liste des règles qui permettent de construire la phrase. Avec cette liste on va créer l'AST

def parse(list_tokens,lexical_table) :
    pile = []
    #on empile l'axiome de la grammaire
    pile.append("F")
    
    token_lu = list_tokens[0]
    sommet_pile = pile.pop()

    regle_list = []
    succes = False 
    erreur = False

    while not(succes or erreur) :
        
        #on arrive à la fin du code source, on peut soit rajouter un token $ à la fin du code source soit dire que si on est à la fin de la liste de token et que la pile est vide alors on a réussi
        if (token_lu=='$' and sommet_pile=='$'):
            succes == True 
            
        #
        elif (token_lu==sommet_pile and token_lu!='$'):
            
            dépiler(token_lu)
            lecture(sommet_pile)

        elif (not terminal(token_lu)) :
            if (table[token_lu,a] != 0):
                regle.append(table[token_lu,a])
                dépiler(token_lu)
                empiler_n(table[token_lu,a])
        else :
            erreur = True

#il faut traiter les erreurs correctement et construire les fonctions nécessaires.



    
   

            





