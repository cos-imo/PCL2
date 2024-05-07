import os
import sys
from collections import deque

class assembly_generator:

    def __init__(self, arbre, tds, forcewrite: True, table_lexicale):
        """
        Variable contenant le numéro de ligne (du fichier assembleur) actuel
            0: ligne data
            1: ligne instruction
            2: ligne fonctions
        """
        self.line_index = [8, 5, 5]


        self.data_index = 0
        self.instruction_index = 7
        self.last_line_index = 8 

        # Dictionnaire contenant les addresses des variables, de la forme {'nom_de_la_variable': 'addresse'}
        self.variables_addresses = {}

        self.arbre = arbre

        self.tds = tds

        self.indentation_level = 0

        """
        Variable contenant le nombre de blocs existants, afin de pouvoir les différencier:
            0. if blocks
            1. 
        """
        self.blocks_number = [0]

        self.writing_flags = [0 for i in range(4)]

        self.generated = []

        self.table_lexicale = table_lexicale

        ### Création du fichier de code assembleur
        ## Création du dossier s'il n'existe pas déjà au préalable
        if os.path.exists("asm_output"):
            pass
        else:
            os.mkdir("asm_output")

        if forcewrite: 
            ## Création du fichier
            # On vérifie si le fichier n'existe pas déjà
            if os.path.exists("asm_output/output.s"):
                sys.stdout.write("[!] Attention! Un fichier 'output.s' est déjà présent dans le répertoire 'asm_output'.\n\tVoulez-vous tout de même lancer la génération de code assembleur?\n\tNOTE: Cela écrasera les données pré-existantes\n")
                self.file_exists()
        with open("assembly/program_template/program_template.s", "r") as file:
            self.data = file.readlines()

        self.generate_assembly()

        # On écrit dans le fichier
        self.write_file()

    def file_exists(self):
        sys.stdout.write("\t(Oui/Non) >>> ")
        response = input()
        if response in ['n', 'non', 'N', 'Non', 'NON']:
            sys.stdout.write("[+] Annulation\n")
            exit()
        elif response in ["o", "oui", "O", "Oui", "OUI"]:
            sys.stdout.write("[+] Suppression de output.s...\n")
            os.remove("asm_output/output.s")
        else:
            self.file_exists()


    def add_function(self, function_name):
        with open("assembly/snippets/calling_frame.s", 'r') as code:
            snippet = [element.replace("<FUNCTION_NAME>", function_name).replace("<RETURN_SIZE>", "X") for element in code.readlines()]
        self.data = self.data[:self.line_index[1]] + snippet + self.data[self.line_index[1]:]
        self.line_index[1] += 4

    def add_procedure(self, function_name):
        with open("assembly/snippets/calling_frame.s", 'r') as code:
            snippet = [element.replace("<FUNCTION_NAME>", function_name).replace("<RETURN_SIZE>", "0") for element in code.readlines()]
        self.data = self.data[:self.line_index[1]] + snippet + self.data[self.line_index[1]:]
        self.line_index[1] += 4

    def add_variable(self, variable_name, variable_value, variable_type):
        if variable_type == "string":
            declaration = "\t.asciz " + variable_value
        elif variable_type == "integer":
            #if variable_value: pourquoi on a des values nul part???
            declaration = f"\t{variable_name}\tDW\t{variable_value}\n"
            #else:
             #   declaration = f"\t{variable_name}\tRSW\n"
        self.data = self.data[:self.line_index[0]] + [declaration] + self.data[self.line_index[0]:]
        for i in range(len(self.line_index)):
            self.line_index[i]+=1

    def initialize_variables(self, variables_liste):
        for element in variables_liste:
            self.add_variable(self.tds.tds_data[element].name, self.tds.tds_data[element].value, self.tds.tds_data[element].type)

    def update_line_index(self, offset):
        pass

    def write_file(self):
        with open("asm_output/output.s", "a") as file:
            for line in self.data:
                file.write(line)

    def generate_assembly(self):
        variables = [element for element in self.tds.tds_data if self.tds.tds_data[element].__repr__().split("(")[0] == "variable"]
        self.initialize_variables(variables)
        self.dfs(self.arbre)

    def write_assembly(self, element):

        if self.writing_flags[0]:
            self.add_procedure(element.value)
            self.writing_flags[0] = 0

        if self.writing_flags[1]:
            self.add_function(element.value)
            self.writing_flags[1] = 0

        if element.fct=="Keyword":
            if element.value == "procedure":
                self.writing_flags[0] = 1
                return
            elif element.value =="function":
                self.writing_flags[1] = 1
                return
        if element.fct== "Ident":
            if element.value not in self.generated:
                pass
        if element.fct == "INSTR":
                if element.children[0].fct == "Ident":
                    if element.children[1].value == ":=":
                        print("assignation")
                        # calculer membre de droite
                        # assigner valeur dans membre de gauche
                elif element.children[0].fct == "Keyword":
                    if element.children[0].value == "if":
                        print("if statement")
                    elif element.children[0].value == "while":
                        print("while loop")
                    elif element.children[0].value == "for":
                        print("for loop")

    def dfs(self, node):
        self.write_assembly(node)

        for child in node.children:
            self.dfs(child)

    def reset_flags(self):
        self.writing_flags = [0 for i in range(4)]

if __name__ == "__main__":
    gene = assembly_generator()
