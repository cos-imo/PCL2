import os
import re

from .symbole import *
from .semantics_controls import * 


class table:
    def __init__(self):
        self.path = ["F"]
        self.tds= {"F":{}}
        self.block_tokens = {(0,8) : "function", (0,18): "procedure", (0,2):"begin", (0,7):"for", (0,9):"loop", (0,27):"while"}
        self.end_tokens = {(0,5): "end"}
        self.variables_tokens = {}

    def create_block(self, block_name):
        current_node = self.tds
        for element in self.path:
            if element not in current_node :
                return ("Problème dans le path de la table des symboles.")
            current_node = current_node[element]
        if block_name in current_node:
            current_node[block_name+str((current_node.count(block_name)+1))] = {}
        else:
            current_node[block_name + "0"] = {}

    def import_token(self, entry):
        if entry in self.block_tokens:
            # Ajouter une entrée "bloc" dans la TDS
            block = self.get_current_bloc()
            if self.enum_bloc(block):
                for element in self.enum_bloc(block):
                    #print(f"element name: {element}")
                    pass
                name = self.block_tokens[entry] + str(self.countRegEx(block, self.block_tokens[entry]))
            else:
                #print("bloc vide")
                pass
        elif entry in self.end_tokens:
            self.import_end_tokens()
        elif entry in self.variables_tokens:
            self.import_variables_tokens(entry)

    def enum_bloc(self, bloc):
        if type(bloc) == fonction:
            pass
        #print("fonction")
        #print(type(bloc))
        
    def import_function(self, function):
        block = self.get_current_bloc()
        self.path.append(function.name) 
        if type(block)==dict:
            block[function.name] = function
        elif type(block)==fonction:
            block.sous_bloc = function
        pass
        #block = self.getBloc()

    def import_end_tokens(self):
        #self.path.pop()
        pass

    def import_variables_tokens(self, variable):
        block = self.get_current_bloc()
        if type(block)==dict:
            block[variable.name] = variable
        elif type(block)==fonction:
            block.sous_bloc[variable.name]=variable


    def add_value(self, entry):
        current_node = self.tds
        for element in self.path:
            current_node = current_node[element]
        if (sc.variableImbricationControle(current_node, entry[1], self.path)): ############################### A modifier, pour faire fonctionner
            print(f"Erreur: la variable {entry[1]} existe déjà.")
        else :
            current_node[entry[0]] = entry[1] 
    
    def add_function(function_name, params_type, return_type):
        return

    
    def get_current_bloc(self):
        current_node = self.tds
        for element in self.path:
            if type(current_node)==dict:
                current_node = current_node[element]
            elif type(current_node)==fonction:
                current_node = current_node.sous_bloc
            else:
                print("bloc non reconnu (get_current_bloc):")
                print(current_bloc)
        return current_node

    def get(self, entry_key):
        if self.tds:
            current_node = self.tds
            if entry_key in current_node:
                return current_node[entry_key]
            else:
                # Ouais bon là je sais pas mais faut explorer récursivement
                pass
    
    def countRegEx(self, lst, expr):
        return len([element for element in lst if re.search(expr, element)])

    def extract_repr(self, node):
        repr_str = "{"
        for element in node:
            if type(element)==variable:
                repr_str += element.__repr__()
            else:
                repr_str += element.__repr__()
                repr_str += (":{" + self.extract_repr(element) + "}")
        repr_str += "}"
        return repr_str

    def __repr__(self):
        print(self.tds)
        print(self.tds["F"]["undebut"].sous_bloc)
        return "ok"
        repr_str = self.extract_repr(self.tds)
        return repr_str
