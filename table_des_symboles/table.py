import sys

class table:
    def __init__(self):
        self.table = []
        self.path=["F"]
        self.table={"F":{}}

    def create(self, table_name):
        current_node = self.table
        for element in path:
            current_node = current_node[element]
            # Gérer l'erreur
        if table_name in current_node:
            current_node[table_name+str((current_node.count(table_name)+1))] = {}
        else:
            current_node[table_name + "0"] = {}

    def add_token(self, entry):
        print(entry[0])
        print(entry[1])
        #current_node = self.table
        #for element in path:
        #    current_node = current_node[element]
        #current_node[entry_key] = entry_value

    def get(self, entry_key):
        if self.table:
            current_node = self.table
            if entry_key in current_node:
                return current_node[entry_key]
            else:
                # Ouais bon là je sais pas mais faut explorer récursivement
                pass

    def __str__(self):
        return "Salut, je suis une TDS"
