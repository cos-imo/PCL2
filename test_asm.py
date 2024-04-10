import unittest

from lexeur.lexeur import lexical_analysis
from parseur.table_syntaxique import table_syntaxique
from parseur.ast_pars import parseur, construire_arbre
from parseur.ast_pars import elaguer, export_tds
from assembly.asm_generator.assembly_generator import *

import parseur.show as show


class MyTestCase(unittest.TestCase):
    def test_pres(self):
        with open("tests/test_pres.txt") as f:
            source_code = f.read()

        tok, lex = lexical_analysis(source_code)
        arbre = construire_arbre(parseur(tok, lex, table_syntaxique))

        tds = export_tds()

        generator =  assembly_generator(tds) 

if __name__ == '__main__':
    unittest.main()
