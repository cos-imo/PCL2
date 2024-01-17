import networkx as nx

from old.parseur.ast_pars import est_terminal

def create_tree(rules):
    """
    return the ast for a program
    :param rules: the grammar rule
    :return: a dict constituting the ast
    """
    G = nx.DiGraph()
    G.add_node(rules[0][0])
    queue = [rules[0][0]]

    for i in range(len(rules)):
        current = queue.pop()

        if est_terminal(current):
            G.add_node(rules[i][1])
            G.add_edge(current, rules[i][1])
        elif rules[i][1] == "epsilon":
            pass
        else:
            for j in range(len(rules[i][1])):
                G.add_node(rules[i][1][j])
                G.add_edge(current, rules[i][1][j])

                queue.append(rules[i][1][j])

    return G

