import unittest
from lexer.lexer import lexer

class MyTestCase(unittest.TestCase):
    def test_lexer(self):
        with open("test_file/test1.txt") as file:
            source_code = file.read()

if __name__ == '__main__':
    unittest.main()
