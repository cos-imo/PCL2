import unittest

from lexeur.lexeur import lexical_analysis


class MyTestCase(unittest.TestCase):
    def test_lexeur_error(self):
        with open("tests/test_lexeur/forbiddenAscii") as f:
            source_code = f.read()




if __name__ == '__main__':
    unittest.main()
