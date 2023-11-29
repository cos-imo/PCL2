class ParseTreeNode:
    def __init__(self, type, children=None, value=None):
        self.type = type
        self.children = children if children is not None else []
        self.value = value

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f"Node({self.type}, value={self.value}, children={self.children})"

#Rappel de la table lexicale:
#init the lexical table with 0 as keywords, 1 as operator, 2 as syntax operator, 3 as identifier, 4 as constant number, 5 invalid char

#Debut du perseur
def parse(tokens, lexical_table):
    current_token_index = 0
    succes = False 
    erreur = False
    pile = []
    pile.append("$")
    pile.append("F")
    

    def next_token():
        # Avance le curseur de lecture
        nonlocal current_token_index
        current_token_index += 1
        if current_token_index < len(tokens):
            current_token = tokens[current_token_index - 1]
            
            
    def peek_token():
        # Regarde le prochain token sans avancer le curseur
        return tokens[current_token_index] if current_token_index < len(tokens) else None



    def parse_F():
        # Logique pour le non-terminal F
        node = ParseTreeNode("F")
        # Implémenter la règle de grammaire pour F
        #F → with adatext_io; use adatext_io; procedure ID is DE begin ISP end IDB ; eof
        if current_token[1] == "with":
            node.add_child(ParseTreeNode("with"))
            next_token()
            if current_token[1] == "adatext_io":
                node.add_child(ParseTreeNode("adatext_io"))
                next_token()
                if current_token[1] == ";":
                    node.add_child(ParseTreeNode(";"))
                    next_token()
                    if current_token[1] == "use":
                        node.add_child(ParseTreeNode("use"))
                        next_token()
                        if current_token[1] == "adatext_io":
                            node.add_child(ParseTreeNode("adatext_io"))
                            next_token()
                            if current_token[1] == ";":
                                node.add_child(ParseTreeNode(";"))
                                next_token()
                                if current_token[1] == "procedure":
                                    node.add_child(ParseTreeNode("procedure"))
                                    next_token()
                                    #On doit lire un identifiant
                                    node.add_child(ParseTreeNode("ID"))
                                    parse_ID()
                                    
                                    next_token()
                                    if current_token[1] == "is":
                                        node.add_child(ParseTreeNode("is"))
                                        next_token()
                                        node.add_child(parse_DE())
                                        if current_token[1] == "begin":
                                            node.add_child(ParseTreeNode("begin"))
                                            next_token()
                                            node.add_child(parse_ISP())
                                            if current_token[1] == "end":
                                                node.add_child(ParseTreeNode("end"))
                                                next_token()
                                                if current_token[1] == "IDB":
                                                    node.add_child(ParseTreeNode("IDB"))
                                                    next_token()
                                                    if current_token[1] == ";":
                                                        node.add_child(ParseTreeNode(";"))
                                                        next_token()
                                                        if current_token[1] == "eof":
                                                            node.add_child(ParseTreeNode("eof"))
                                                            next_token()
                                                            return node
        
        return node

    def parse_ID():
        if current_token[0] == 3:
            

    while current_token_index < len(tokens) and not(erreur or succes):
        current_token = peek_token()
        current_stack_top = pile.pop()
        if current_token == "$" and current_stack_top == "$":
            succes = True
        
        else parse_F()
        

# Utilisation
# tokens = [...] # Liste des tokens générés par le lexeur
# ast = parse(tokens)
# print(ast)
