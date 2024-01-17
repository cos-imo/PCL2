import unittest

from lexeur.lexeur import lexical_analysis


class MyTestCase(unittest.TestCase):
    def test_lexeur_error_forbidAscii(self):
        with open("tests/test_lexeur/forbiddenAscii.txt") as f:
            source_code = f.read()

        print(lexical_analysis(source_code))

    def test_lexeur_error_remWS(self):
        with open("tests/test_lexeur/remWithoutSpace.txt") as f:
            source_code = f.read()

        print(lexical_analysis(source_code))

    def test_lexeur_error_idenBN(self):
        with open("tests/test_lexeur/identBeginNumber.txt") as f:
            source_code = f.read()

        print(lexical_analysis(source_code))


if __name__ == '__main__':
    unittest.main()
