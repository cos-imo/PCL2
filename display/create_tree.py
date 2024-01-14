from display_tree import display_tree

# to create a empty tree :

tree = {}

# you want to add a node to the tree

tree.update({"new_node": []})

# you want to add a chaild to a node

tree["new_node"].append("other_node")

# you want to add a children to a node but you don't know if it exists

if "node" in tree:
    tree["node"].append("other_node")
else:
    tree.update({"node": ["other_node"]})

# you want to display the tree

display_tree(tree)
