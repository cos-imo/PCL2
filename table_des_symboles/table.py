import sys

class table:
    def __init__(self):
        self.table = []

    def create(self):
        table={}
        return table

    def add(selfself, entry_key, entry_value):
        if self.table:
            self.table[entry_key] += entry_value
        else:
            sys.stdout.write("Erreur: Tentative d'ajout à une table inexistante")

    def get(self, entry_key):
        if self.table:
            return self.table[entry_key]