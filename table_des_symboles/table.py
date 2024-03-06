import os
import re

import semantics_controls as sc
from symbole import *


class table:
    def __init__(self):
        self.path = ["F"]
        self.table = {"F":{}}


    def create_block(self, block_name):
        current_node = self.table
        for element in self.path:
            if element not in current_node :
                return ("Problème dans le path de la table des symboles.")
            current_node = current_node[element]
        if block_name in current_node:
            current_node[block_name+str((current_node.count(block_name)+1))] = {}
        else:
            current_node[block_name + "0"] = {}

    def import_token(self, entry):
        block_tokens = {(0,8) : "function", (0,18): "procedure", (0,2):"begin", (0,7):"for", (0,9):"loop", (0,27):"while"}
        end_tokens = {(0,5): "end"}
        variables_tokens = {}
        if entry in block_tokens:
            # Ajouter une entrée "bloc" dans la TDS
            block = self.getBloc(self.path)
            name = block_tokens[entry] + self.countRegEx(block, block_tokens[entry])
        
    def import_function(self, function):
        block = self.getBloc()


    def add_value(self, entry_key, entry_value):
        current_node = self.table
        for element in self.path:
            current_node = current_node[element]
        if (sc.variableImbricationControle(current_node, entry_value, self.path)): ############################### A modifier, pour faire fonctionner
            print(f"Erreur: la variable {entry_value} existe déjà.")
        else :
            current_node[entry_key] = entry_value
    
    def add_function(function_name, params_type, return_type):
        return
    
    def getBloc(self, pile):
        current_node = self.table
        for element in self.path:
            current_node = current_node[element]
        return current_node

    def get(self, entry_key):
        if self.table:
            current_node = self.table
            if entry_key in current_node:
                return current_node[entry_key]
            else:
                # Ouais bon là je sais pas mais faut explorer récursivement
                pass
    
    def countRegEx(self, list, expr):
        return len([element for element in list if re.search(expr, element)])