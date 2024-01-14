import networkx as nx
import matplotlib.pyplot as plt


def display_tree(to_display: dict):
    graph = nx.from_dict_of_lists(to_display)

    nx.draw(graph)
    plt.show()