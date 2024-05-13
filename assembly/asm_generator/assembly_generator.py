import os
import sys
from collections import deque

class assembly_generator:

    def __init__(self, arbre, tds, forcewrite: True, table_lexicale):

        self.current_placement = "<INSTRUCTIONS>\n"
        self.placement_history = []

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
            1. for loops
            2. while loops
        """
        self.blocks_number = [0, 0, 0]

        self.writing_flags = [0 for i in range(5)]

        self.generated = []

        self.table_lexicale = table_lexicale

        self.dfs_history = []

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

    def write_data(self, code, placement):
        self.data = self.data[:self.data.index(placement)] + code + self.data[self.data.index(placement):]

    def add_function(self, function_name, node):
        with open("assembly/snippets/calling.s", 'r') as code:
            snippet = [element.replace("<FUNCTION_NAME>", function_name) for element in code.readlines()]
        self.write_data(snippet, self.current_placement)
        with open("assembly/snippets/function_frame.s", 'r') as code:
            snippet = [element.replace("<FUNCTION_NAME>", function_name).replace("<RETURN_SIZE>", "2") for element in code.readlines()]
        self.write_data(snippet, "<FUNCTIONS>\n")

        self.placement_history.append(self.current_placement)
        self.current_placement = "  <FUNCTION_CODE>\n"

    def add_procedure(self, function_name, node):
        with open("assembly/snippets/calling.s", 'r') as code:
            snippet = [element.replace("<FUNCTION_NAME>", function_name).replace("<RETURN_SIZE>", "2") for element in code.readlines()]
        self.write_data(snippet, self.current_placement)
        with open("assembly/snippets/function_frame.s", 'r') as code:
            snippet = [element.replace("<FUNCTION_NAME>", function_name).replace("<RETURN_SIZE>", "2") for element in code.readlines()]
        self.write_data(snippet, "<FUNCTIONS>\n")

        self.placement_history.append(self.current_placement)
        self.current_placement = "  <FUNCTION_CODE>\n"

    def add_variable(self, variable_name, variable_value, variable_type):
        if variable_type == "string":
            declaration = "\t.asciz " + variable_value
        elif variable_type == "integer":
            if variable_value: #pourquoi on a des values nul part???
                declaration = f"\t{variable_name}\tDW\t{variable_value}\n"
            else:
                declaration = f"\t{variable_name}\tRESW\t1\n"
        self.write_data([declaration], "<DATA>\n")

    def add_assignation(self, variable, value):
        with open("assembly/snippets/assignation.s", 'r') as code:
            snippet = [element.replace("<VALUE>", value).replace("<VARIABLE>", variable) for element in code.readlines()]
        self.write_data(snippet, self.current_placement)

    def add_for_loop(self, for_node):
        numero_bloc = self.blocks_number[1]

        self.blocks_number[1] += 1

        self.write_data([f"  call begin_for_loop_{numero_bloc}\n\n"], self.current_placement)

        self.placement_history.append(self.current_placement)
        self.current_placement = "  <FUNCTION_CODE>\n"

        with open("assembly/snippets/for_loop.s") as code:
            snippet = [element.replace("X", str(numero_bloc)).replace("<var_indice_start>", str(for_node.children[3].value)).replace("<var_indice_stop>", str(for_node.children[5].value)) for element in code.readlines()]

        self.write_data(snippet, self.current_placement)

        self.placement_history.append(self.current_placement)
        self.current_placement = f"  <FOR_LOOP_CODE_{numero_bloc}>\n"

    def operation(self,element):
        if element.fct == "OPE5" :
            if element.children[0].fct == "Number":
                if element.children[1].children[0].value == "+":
                    if element.children[1].children[1].fct == "Number":
                        with open("assembly/snippets/addition.s", 'r') as code:
                            snippet = [elem.replace("<VALUE1>", str(element.children[0].value)).replace("<VALUE2>", str(element.children[1].children[1].value)) for elem in code.readlines()]
                        self.write_data(snippet, self.current_placement)

    def initialize_variables(self, variables_liste):
        for element in variables_liste:
            self.add_variable(self.tds.tds_data[element].name, self.tds.tds_data[element].value, self.tds.tds_data[element].type)

    def write_file(self):
        self.data = [element for element in self.data if ((element not in ["<DATA>\n", "<FUNCTIONS>\n", "<INSTRUCTIONS>\n", "  <FUNCTION_CODE>\n"]) and ("FOR_LOOP_CODE_" not in element))]
        with open("asm_output/output.s", "a") as file:
            for line in self.data:
                file.write(line)

    def generate_assembly(self):
        variables = [element for element in self.tds.tds_data if self.tds.tds_data[element].__repr__().split("(")[0] == "variable"]
        self.initialize_variables(variables)
        self.dfs(self.arbre)

    def write_assembly(self, element):

        if self.writing_flags[0]:
            self.add_procedure(element.value, element)
            self.writing_flags[0] = 0

        if self.writing_flags[1]:
            self.add_function(element.value, element)
            self.writing_flags[1] = 0

        if self.writing_flags[4]:
            self.current_placement = self.placement_history[-1]
            self.placement_history.pop()
            self.writing_flags[4] = 0

        if element.fct=="Keyword":
            if element.value == "procedure":
                self.writing_flags[0] = 1
                return
            elif element.value =="function":
                self.writing_flags[1] = 1
                return
            elif element.value == "end":
                self.writing_flags[4] == 1
        if element.fct== "Ident":
            if element.value not in self.generated:
                pass
        if element.fct == "INSTR":
                if element.children[0].fct == "Ident":
                    if element.children[1].value == ":=":
                        self.add_assignation(element.children[0].value, str(element.children[2].value))
                        # on print l'assignation
                        print(f"{element.children[0].value} := {element.children[2].value}") ##########################################################
                        pass
                        # calculer membre de droite
                        # assigner valeur dans membre de gauche
                elif element.children[0].fct == "Keyword":
                    if element.children[0].value == "if":
                        print("if statement")
                    elif element.children[0].value == "while":
                        print("while loop")
                    elif element.children[0].value == "for":
                        self.add_for_loop(element)
        if element.fct[:3] == "OPE":
            self.operation(element)

    def dfs(self, node):
        self.write_assembly(node)

        for child in node.children:
            if child not in self.dfs_history:
                self.dfs(child)
                self.dfs_history.append(child)

if __name__ == "__main__":
    gene = assembly_generator()
