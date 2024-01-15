class Node:
    def __init__(self, fct, children=None, value=None):
        """
        Initialise un nouveau nœud de l'arbre.

        :param type: Type de nœud (par exemple, 'Add', 'Subtract', 'Number', 'Identifier', etc.)
        :param children: Liste des nœuds enfants (sous-arbres).
        :param value: Valeur du nœud (utile pour les feuilles comme les nombres ou les identifiants).
        """
        self.fct = fct
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
        return f"Node({self.fct}, children={self.children}, value={self.value})"

#def prune(tree) : 
def elaguer_arbre(node):
    # Élaguer récursivement les enfants d'abord
    children_to_keep = []
    for child in node.children:
        pruned_child = elaguer_arbre(child)
        if pruned_child or (child.value is None and any(isinstance(grandchild.value, tuple) for grandchild in child.children)):
            children_to_keep.append(child)
    
    # Mettre à jour les enfants après l'élagage
    node.children = children_to_keep
    
    # Si après l'élagage il ne reste aucun enfant et que la valeur du nœud est élagable, élaguer le nœud
    if not node.children and node.value in (None, "epsilon"):
        return None  # Le nœud est élagable

    return node  # Garder le nœud


def remonter_feuilles(node):
    # Si le nœud a exactement un enfant et que la valeur du nœud est None, remonter cet enfant
    if len(node.children) == 1 and node.value is None:
        return remonter_feuilles(node.children[0])

    # Sinon, appliquer la fonction récursivement à tous les enfants
    new_children = []
    for child in node.children:
        new_child = remonter_feuilles(child)
        if new_child:
            new_children.append(new_child)
    
    node.children = new_children

    return node