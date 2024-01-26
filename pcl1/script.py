from lexeur.lexeur import lexical_analysis
from parseur.ast_pars import construire_arbre, parse, elaguer, Node
from parseur.table_syntaxique import table_syntaxique


def pcl1(source_code: str) -> Node:
    """
    Make all that should be done in pcl part. 1. Lex, parse, create a tree and reduce it
    :param source_code: the source code that we want to compile 
    :return: the tree that we need to continue the compile program
    """

    token, lexical_table = lexical_analysis(source_code)
    tree = construire_arbre(parse(token, lexical_table, table_syntaxique))
    tree = elaguer(tree)

    return tree
