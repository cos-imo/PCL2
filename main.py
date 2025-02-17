import argparse

from lexeur.lexeur import lexical_analysis
from parseur.ast_pars import Node, construire_arbre, elaguer, parseur
from parseur.table_syntaxique import table_syntaxique
from assembly.asm_generator.assembly_generator import *

import parseur.show as show


class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(usage='python3 source/main.py file_name [OPTIONS]', add_help=False, description='Compile un programme Ada')
        self.parse_arguments()

    def parse_arguments(self):
        self.parser.add_argument('sourcefile', type=open)

        self.parser.add_argument('-h','--help', action='help', help="Affiche ce message d'aide")
        self.parser.add_argument('-v','--verbose', help="Active le mode verbose")
        self.parser.add_argument('-T', '--tree', help="Affiche l'arbre")
        self.parser.add_argument('-a', '--assembly', help="Génère le code assembleur")
        self.parser.add_argument('-d', '--debug', help="Active le mode débogueur")
        self.parser.add_argument('-f', '--forcewrite', help="Ecrase l'éventuel fichier assembleur pré-existant")

        self.args = self.parser.parse_args()


def pcl1(source_code: str) -> Node:
    """
    Make all that should be done in pcl part. 1. Lex, parse, create a tree and reduce it
    :param source_code: the source code that we want to compile 
    :return: the tree that we need to continue the compile program
    """

    token, lexical_table = lexical_analysis(source_code)
    parseur_obj = parseur(token, lexical_table, table_syntaxique)
    tree = elaguer(construire_arbre(parseur_obj))

    if parser.args.tree:
        arbre_élagué = elaguer(tree)
        show.afficher(arbre_élagué, 'LR', 'test_pres_syntax_tree_elagué_LR', './output/reduced')
        show.afficher(arbre_élagué, '', 'test_pres_syntax_tree_elagué', './output/reduced')

    if parser.args.assembly:
        if parser.args.forcewrite:
            assembly = assembly_generator(tree, parseur_obj[1], False, lexical_table)
        else:
            assembly = assembly_generator(tree, parseur_obj[1], True, lexical_table)


    if parser.args.debug:
        print(elaguer(construire_arbre(parseur(token, lexical_table, table_syntaxique))))

    return tree

if __name__=="__main__":
    parser=Parser()

    data=parser.args.sourcefile.read()

    pcl1(data)
