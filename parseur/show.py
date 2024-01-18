from graphviz import Digraph


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


def visualize_tree(node, graph=None, orentation='TB'):
    if graph is None:
        graph = Digraph(format='png')  # Vous pouvez choisir un format différent si vous le souhaitez

    graph.node(str(id(node)), label=f"{node.fct}\n{node.value}")

    for child in node.children:
        visualize_tree(child, graph)
        graph.edge(str(id(node)), str(id(child)))

    return graph


def visualize_tree_hor(node, graph=None, orientation='TB'):
    if graph is None:
        graph = Digraph(format='png', graph_attr={'rankdir': orientation})

    graph.node(str(id(node)), label=f"{node.fct}\n{node.value}")

    for child in node.children:
        visualize_tree(child, graph, orientation)
        graph.edge(str(id(node)), str(id(child)))

    return graph


def inverser_enfants_arbre(node):
    if node.children:
        node.children.reverse()  # Inverser l'ordre des enfants du nœud courant
        for enfant in node.children:
            inverser_enfants_arbre(enfant)  # Répéter récursivement pour chaque enfant

# # Exemple d'utilisation :
# root = Node('Root', [
#     Node('Add', [
#         Node('Number', value='2'),
#         Node('Multiply', [
#             Node('Number', value='3'),
#             Node('Identifier', value='x')
#         ])
#     ]),
#     Node('Assign', [
#         Node('Identifier', value='y'),
#         Node('Subtract', [
#             Node('Number', value='5'),
#             Node('Number', value='2')
#         ])
#     ])
# ])
