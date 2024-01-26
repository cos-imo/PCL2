import unittest

from lexeur.lexeur import lexical_analysis
from parseur.table_syntaxique import table_syntaxique
from parseur.ast_pars import parseur, construire_arbre
from parseur.ast_pars import elaguer

import parseur.show as show


class MyTestCase(unittest.TestCase):
    def test_pres(self):
        with open("tests/test_pres.txt") as f:
            source_code = f.read()

        tok, lex = lexical_analysis(source_code)
        arbre = construire_arbre(parseur(tok, lex, table_syntaxique))

        show.afficher(arbre, 'LR', 'test_pres_syntax_tree_LR', './output/basic')
        show.afficher(arbre, '', 'test_pres_syntax_tree', './output/basic')

        arbre_elaguer = elaguer(arbre)

        show.afficher(arbre_elaguer, 'LR', 'test_pres_syntax_tree_elaguer_LR', './output/reduced')
        show.afficher(arbre_elaguer, '', 'test_pres_syntax_tree_elaguer', './output/reduced')

if __name__ == '__main__':
    unittest.main()
