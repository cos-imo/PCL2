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
    
    def remove_child(self, child):
        """
        Supprime un enfant de ce nœud.

        :param child: Nœud enfant à supprimer.
        """
        self.children.remove(child)

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
    if not node.children and node.value in (None, "epsilon",";", "(", ")",",",":"):
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



def inverser_enfants_arbre(node):
    if node.children:
        node.children.reverse()  # Inverser l'ordre des enfants du nœud courant
        for enfant in node.children:
            inverser_enfants_arbre(enfant)  # Répéter récursivement pour chaque enfant


# remove unles node like ";" "(" ")"
def remove_unless_node(node):
    # Élaguer récursivement les enfants d'abord
    children_to_keep = []
    for child in node.children:
        pruned_child = remove_unless_node(child)
        if pruned_child or (child.value is None and any(isinstance(grandchild.value, tuple) for grandchild in child.children)):
            children_to_keep.append(child)
    
    # Mettre à jour les enfants après l'élagage
    node.children = children_to_keep
    
    # Si après l'élagage il ne reste aucun enfant et que la valeur du nœud est élagable, élaguer le nœud
    if not node.children and node.value in (";", "(", ")"):
        return None  # Le nœud est élagable

    return node  # Garder le nœud


def remonter_param(node):
    # Si le noeud est une feuille (il n'a pas d'enfant) ne rien faire 
    if not node.children:
        return node
    
    # Si les enfants du noeud sont des feuilles (ils n'ont pas d'enfant) ne rien faire
    if not any(child.children for child in node.children):
        return node
    
    # Si un enfant du noeud est "PARAM_POINT_VIRG_PLUS" 
    # On remplace ce noeud par les enfants de "PARAM_POINT_VIRG_PLUS"
    # On ajoute les noeuds dans l'ordre

    new_children = [] 
    for i in range(len(node.children)):
        if node.children[i].fct == "PARAM_POINT_VIRG_PLUS":
            new_children = node.children[:i] + node.children[i].children +  node.children[i+1:]
            node.children = new_children
            return node
        else :
            remonter_param(node.children[i])

def replace_param_point_virg_plus(root_node):
    def replace_recursive(node, parent, index):
        if node.fct == "PARAM_POINT_VIRG_PLUS" or node.fct == "DECL_STAR":
            # Supprimer le nœud "PARAM_POINT_VIRG_PLUS" du parent
            parent.children.pop(index)

            # Ajouter les nœuds "PARAM" à la place de "PARAM_POINT_VIRG_PLUS"
            for param_node in node.children:
                parent.children.insert(index, param_node)
                index += 1

        # Parcourir récursivement les enfants du nœud actuel
        for i, child in enumerate(node.children):
            replace_recursive(child, node, i)

    # Créer un nœud factice pour représenter la racine parente du nœud racine réel
    fake_root = Node("FAKE_ROOT", children=[root_node])

    # Appeler la fonction récursive avec le faux nœud racine
    replace_recursive(fake_root, None, None)

    # Mettre à jour le nœud racine réel en utilisant le seul enfant du faux nœud racine
    root_node = fake_root.children[0]
            

