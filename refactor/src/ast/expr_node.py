"""Node that represent expression in the AST"""

from ast import Node


class ExprNode(Node):
    """Base class for the expression"""
    def __init__(self):
        super().__init__()

    def gen_il_or_asm(self, ilCode, symbolTable, context):
        """
        Future func to generate intermediate code for the node
        :param ilCode: The il code where we will add generated node il code
        :param symbolTable: The symbol table for the current node
        :param context: Context for the current node if necessary
        """
        raise NotImplementedError


