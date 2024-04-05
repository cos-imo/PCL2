"""Classes for the declarations nodes"""
from ast import Node


class DeclNode(Node):
    """Base class for the declarations block"""
    pass


class Root(DeclNode):
    """Represents a list of declaration specifiers and declarators"""
    def __init__(self, specs, decls, inits=None):
        super().__init__()
        self.specs = specs
        self.decls = decls
        self.inits = inits if inits else [None] * len(self.decls)


class Access(DeclNode):
    """Create access (pointer) node"""
    pass


class Function(DeclNode):
    """
    Represents a function with given arguments and returning type
    args: List(Node) - arguments of the functions
    """
    def __init__(self, args, child):
        """Generate function node"""
        super().__init__()
        self.args = args
        self.child = child

class Identifier(DeclNode):
    """
    Represents an identifier
    If this it is a type name without identifier, 'identifier' is None
    """
    def __init__(self, identifier):
        """Generate an identifier node from identifier"""
        super().__init__()
        self.identifier = identifier


class Class(DeclNode):
    """Generate a class node"""
    def __init__(self):
        pass
