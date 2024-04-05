"""Nodes of the AST that are statements or declarations"""


class Node:
    """Base class for AST node"""

    def __int__(self):
        self.r = None

    def gen_il_or_asm(self, ilCode, symbolTable, context):
        """
        Future func to generate intermediate code for the node
        :param ilCode: The il code where we will add generated node il code
        :param symbolTable: The symbol table for the current node
        :param context: Context for the current node if necessary
        """
        raise NotImplementedError


class Root(Node):
    """The root node of our AST"""

    def __int__(self, nodes):
        super().__int__()
        self.nodes = nodes

    def gen_il_or_asm(self, ilCode, symbolTable, context):
        """Make code for the root"""
        pass


class Compound(Node):
    """
    Create a node of a compound statement
    :param items: The inside of the compound statement
    """

    def __int__(self, items):
        super().__int__()
        self.items = items

    def gen_il_or_asm(self, ilCode, symbolTable, context):
        """Make code for every item block inside the compound"""
        pass


class Return(Node):
    """
    Create the node for a return statement
    :param returnValue: The value to return
    """

    def __int__(self, returnValue):
        super().__int__()
        self.returnValue = returnValue

    def gen_il_or_asm(self, ilCode, symbolTable, context):
        """Make code for the return value"""
        pass


class ExprStatement(Node):
    """
    Create a node for a single expression
    expr - The expression
    """

    def __int__(self, expr):
        super().__int__()
        self.expr = expr

    def gen_il_or_asm(self, ilCode, symbolTable, context):
        """Make code for the expression"""
        pass


class IfStatement(Node):
    """
    Create the node for the if statement
    :param cond: The condition to execute the if statement
    :param statement: The statement inside the if block
    :param elseStatement: The statement inside the else block
    """

    def __int__(self, cond, statement, elseStatement):
        super().__int__()
        self.cond = cond
        self.statement = statement
        self.elseStatement = elseStatement

    def gen_il_or_asm(self, ilCode, symbolTable, context):
        """Make code for the if-else statement"""
        pass


class Loop(Node):
    """
    Create the node for the loop
    :param name: The name of the loop
    :param cond: The exit condition of the loop
    :param statement: The statement of the loop
    """

    def __int__(self, name, cond, statement):
        super().__int__()
        self.name = name
        self.cond = cond
        self.statement = statement

    def gen_il_or_asm(self, ilCode, symbolTable, context):
        """Make code for the loop"""
        pass


class WhileStatement(Node):
    """
    Create the node for the while loop
    :param cond: The condition of the while loop
    :param statement: The statement of the while loop
    """

    def __int__(self, cond, statement):
        super().__int__()
        self.cond = cond
        self.statement = statement

    def gen_il_or_asm(self, ilCode, symbolTable, context):
        """Make code for the while loop"""
        pass


class ForStatement(Node):
    """
    Create the node for the for loop
    :param param: The parameter of our for loop
    :param first: The first value of our parameter
    :param last: The last value of our parameter
    """

    def __int__(self, param, first, last):
        super().__int__()
        self.param = param
        self.first = first
        self.last = last

    def gen_il_or_asm(self, ilCode, symbolTable, context):
        """Make code for the for loop"""
        pass


class Declaration(Node):
    """
    Create a node for a general declaration
    :param node: A declaration tree for the node
    :param body: The body if we declare a function or a procedure
    """

    def __int__(self, node, body):
        super().__int__()
        self.node = node
        self.body = body

    def gen_il_or_asm(self, ilCode, symbolTable, context):
        """Make code for the declaration"""
        pass
