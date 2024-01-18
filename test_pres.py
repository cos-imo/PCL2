import unittest

from lexeur.lexeur import lexical_analysis
from parseur.table_syntaxique import table_syntaxique
from parseur.ast_pars import parseur, construire_arbre
from parseur.ast_pars import elaguer_arbre, remonter_feuilles, remove_unless_node, \
    remove_intermediary_node

import parseur.show as show


class MyTestCase(unittest.TestCase):
    def test_pres(self):
        with open("tests/test_pres.txt") as f:
            source_code = f.read()

        tok, lex = lexical_analysis(source_code)
        arbre = construire_arbre(parseur(tok, lex, table_syntaxique))

        show.visualize_tree(arbre).render(filename='syntax_tree', directory='./output/basic', cleanup=True,
                                          format='png',
                                          engine='dot')
        show.visualize_tree_hor(arbre, orientation='LR').render(filename='syntax_tree_hor', directory='./output/basic',
                                                                cleanup=True, format='png', engine='dot')

        arbre = remonter_feuilles(elaguer_arbre(arbre))
        remove_intermediary_node(arbre)
        remove_unless_node(arbre)

        show.visualize_tree(arbre).render(filename='prun_param_syntax_tree_param', directory='./output/reduced',
                                          cleanup=True, format='png', engine='dot')
        show.visualize_tree_hor(arbre, orientation='LR').render(filename='prun_param_syntax_tree_param_hor',
                                                                directory='./output/reduced', cleanup=True,
                                                                format='png',
                                                                engine='dot')


if __name__ == '__main__':
    unittest.main()
