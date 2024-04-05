"""
Logic that parses the declaration nodes
"""


def parse_func_definition(index):
    """Parse a function definition"""
    pass


def parse_decls_specifiers(index):
    """
    Parse declarations initializers
    -> a: int
    """
    pass


def parse_parameter_list(index):
    """Parse a function parameter list"""
    pass


def parse_class(index):
    """Parse a class specifier"""
    pass


def parse_class_members(index):
    """Parse a list of members of a class"""
    pass


# add token_kinds lorsqu'il seront remplie open, close, mess qui return mismatched error
def find_pair_forward(index):
    """Find the closing parenthesis for the opening at a given index"""
    pass


# add token_kinds lorsqu'il seront remplie open, close, mess qui return mismatched error
def find_pair_backward(index):
    """Find the opening parenthesis for the opening at a given index"""
    pass


def find_decl_end(index):
    """Find the end of the declarator that start at a given index"""
    pass


def parse_declarator(start, end):
    """Parse a declarator between start and end"""
    pass


def trry_parse_func_dcl(start, end):
    """Parse a func declaration between start and end"""
    pass
