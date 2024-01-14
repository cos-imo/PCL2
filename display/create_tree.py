from display_tree import display_tree
from parseur.ast_pars import est_terminal

# to create a empty tree :

tree = {}

# you want to add a node to the tree

tree.update({"new_node": []})

# you want to add a chaild to a node

tree["new_node"].append("other_node")

# you want to add a children to a node, but you don't know if it exists

if "node" in tree:
    tree["node"].append("other_node")
else:
    tree.update({"node": ["other_node"]})

tree["node"].append(1)
tree.update({"other_node": [1]})

# you want to display the tree

display_tree(tree)


def create_tree(rules):
    """
    return the ast for a program
    :param rules: the grammar rule
    :return: a dict constituting the ast
    """
    ast = {rules[0][0]: []}
    queue = [rules[0][0]]

    for i in range(len(rules)):
        current = queue.pop(0)

        if est_terminal(current):
            current = rules[i][1]
        else:
            for j in range(len(rules[i][1])):
                if current not in ast:
                    ast.update({current: []})
                ast[current].append(rules[i][1][j])


                queue.append(rules[i][1][j])

    return ast
