import sys


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


    def add_value(self, entry_key, entry_value):
        current_node = self.table
        for element in self.path:
            current_node = current_node[element]
        if ("savoir si value est dedans"): ###########################################################################
            print("Erreur: la variable " + entry_value + " existe déjà.")
        else :
            current_node[entry_key] = entry_value


    def get(self, entry_key):
        if self.table:
            current_node = self.table
            if entry_key in current_node:
                return current_node[entry_key]
            else:
                # Ouais bon là je sais pas mais faut explorer récursivement
                pass
    
    
