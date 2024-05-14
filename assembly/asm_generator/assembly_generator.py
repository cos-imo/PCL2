import os
import sys
import re
from collections import deque

cunt_put = 0

class assembly_generator:

    def __init__(self, arbre, tds, forcewrite: True, table_lexicale):
        
        self.current_placement = "<INSTRUCTIONS>\n"
        self.placement_history = []

        self.data_index = 0
        self.instruction_index = 7
        self.last_line_index = 8 

        # Dictionnaire contenant les addresses des variables, de la forme {'nom_de_la_variable': 'addresse'}
        self.variables_addresses = {}

        self.is_writing_function = 0

        self.arbre = arbre

        self.tds = tds

        self.indentation_level = 0

        """
        Variable contenant le nombre de blocs existants, afin de pouvoir les différencier:
            0. if blocks
            1. for loops
            2. while loops
            3. fonctions
        """
        self.blocks_number = [0, 0, 0, 0]

        self.writing_flags = [0 for i in range(7)]

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
            snippet = [element.replace("<FUNCTION_NAME>", function_name).replace("<RETURN_SIZE>", "16").replace("<FUNCTION_CODE>", f"<FUNCTION_{self.blocks_number[3]}_CODE>") for element in code.readlines()]
        self.write_data(snippet, "<FUNCTIONS>\n")

        self.placement_history.append(self.current_placement)
        self.current_placement = f"  <FUNCTION_{self.blocks_number[3]}_CODE>\n"

        self.blocks_number[3] += 1

        self.is_writing_function = 1

    def add_put_var(self, var, cunt_put):
        with open("assembly/snippets/put.s", 'r') as code:
            snippet = [element.replace("<VALUE>", "["+var.name+"]").replace("X", str(cunt_put)) for element in code.readlines()]
        self.write_data(snippet, self.current_placement)
        type = self.tds.tds_data[var.name].type
        self.add_var_de_put(type, cunt_put)

    def add_put_cst(self, cst, cunt_put):
        var_name = f"var_print_cst_{cunt_put}"
        type_cst = str(type(cst)).split("'")[1]
        if type_cst == "int":
            type_cst = "integer"
        else :
            type_cst = "character"
        self.add_variable(var_name, str(cst), type_cst)
        with open("assembly/snippets/put.s", 'r') as code:
            snippet = [element.replace("<VALUE>", "["+var_name+"]").replace("X", str(cunt_put)) for element in code.readlines()]
        self.write_data(snippet, self.current_placement)
        if type(cst) == int:
            declaration = f"\tformat_{cunt_put}\tdb\t\"%d\",\t10,\t0\n"
        else: #elif type(cst) == str:
            declaration = f"\tformat_{cunt_put}\tdb\t\"%s\",\t10,\t0\n"
        self.write_data([declaration], "<DATA>\n")

    def add_var_de_put(self, type, cunt_put):
        param = ""
        if type == "integer":
            param = "d"
        elif type == "character":
            param = "s"
        declaration = f"\tformat_{cunt_put}\tdb\t\"%{param}\",\t10,\t0\n"
        self.write_data([declaration], "<DATA>\n")




    def add_procedure(self, function_name, node):
        with open("assembly/snippets/calling.s", 'r') as code:
            snippet = [element.replace("<FUNCTION_NAME>", function_name).replace("<RETURN_SIZE>", "16") for element in code.readlines()]
        self.write_data(snippet, self.current_placement)
        with open("assembly/snippets/function_frame.s", 'r') as code:
            snippet = [element.replace("<FUNCTION_NAME>", function_name).replace("<RETURN_SIZE>", "16").replace("<FUNCTION_CODE>", f"<FUNCTION_{self.blocks_number[3]}_CODE>") for element in code.readlines()]
        self.write_data(snippet, "<FUNCTIONS>\n")

        self.placement_history.append(self.current_placement)
        self.current_placement = f"  <FUNCTION_{self.blocks_number[3]}_CODE>\n"
        self.blocks_number[3] += 1

    def add_variable(self, variable_name, variable_value, variable_type):
        if variable_type == "string":
            declaration = "\t.asciz " + variable_value
        elif variable_type == "integer":
            if variable_value != None: #pourquoi on a des values nul part???
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

        # Ajouter l'appel à la boucle for générée
        self.write_data([f"  call begin_for_loop_{numero_bloc}\n\n"], self.current_placement)

        # Sauvegarder le placement actuel et passer à la génération de la boucle for
        self.placement_history.append(self.current_placement)
        self.current_placement = "  <INSTRUCTION_BOUCLE>\n"

        # Lire et adapter le code de la boucle for
        with open("assembly/snippets/for_loop.s") as code:
            snippet = [element.replace("X", str(numero_bloc)).replace("<var_indice_start>", str(for_node.children[3].value)).replace("<var_indice_stop>", str(for_node.children[5].value)) for element in code.readlines()]

        # Ecrire le snipper de la boucle for
        self.write_data(snippet, self.current_placement)
        
        
        
        self.current_placement = f"    <FOR_LOOP_CODE_{numero_bloc}>\n"

    def operation(self,element):
        #Si c'est une addition
        if element.fct == "OPE5" :
            if element.children[0].fct == "Number" or element.children[0].fct == "Ident":
                # Cas ou on a une addition de deux nombres ou deux variables
                if element.children[1].children[0].value == "+":
                    if element.children[1].children[1].fct == "Number" or element.children[1].children[1].fct == "Ident":
                        if element.children[0].fct == "Ident" and element.children[1].children[1].fct == "Ident":
                            with open("assembly/snippets/addition.s", 'r') as code:
                                snippet = [elem.replace("<VALUE1>", "["+str(element.children[0].value)+"]").replace("<VALUE2>", "["+str(element.children[1].children[1].value)+"]") for elem in code.readlines()]
                                return snippet
                        elif element.children[0].fct == "Ident" and element.children[1].children[1].fct == "Number":
                            with open("assembly/snippets/addition.s", 'r') as code:
                                snippet = [elem.replace("<VALUE1>", "["+str(element.children[0].value)+"]").replace("<VALUE2>", str(element.children[1].children[1].value)) for elem in code.readlines()]
                                return snippet
                        elif element.children[0].fct == "Number" and element.children[1].children[1].fct == "Ident":
                            with open("assembly/snippets/addition.s", 'r') as code:
                                snippet = [elem.replace("<VALUE1>", str(element.children[0].value)).replace("<VALUE2>", "["+ str(element.children[1].children[1].value)+ "]") for elem in code.readlines()]
                                return snippet
                        else :
                            with open("assembly/snippets/addition.s", 'r') as code:
                                snippet = [elem.replace("<VALUE1>", str(element.children[0].value)).replace("<VALUE2>", str(element.children[1].children[1].value)) for elem in code.readlines()]
                                return snippet
                # Cas ou on a une soustraction de deux nombres ou deux variables
                elif element.children[1].children[0].value == "-":
                    if element.children[1].children[1].fct == "Number" or element.children[1].children[1].fct == "Ident":
                        if element.children[0].fct == "Ident" and element.children[1].children[1].fct == "Ident":
                            with open("assembly/snippets/soustraction.s", 'r') as code:
                                snippet = [elem.replace("<VALUE1>", "["+str(element.children[0].value)+"]").replace("<VALUE2>", "["+str(element.children[1].children[1].value)+"]") for elem in code.readlines()]
                                return snippet
                        elif element.children[0].fct == "Ident" and element.children[1].children[1].fct == "Number":
                            with open("assembly/snippets/soustraction.s", 'r') as code:
                                snippet = [elem.replace("<VALUE1>", "["+str(element.children[0].value)+"]").replace("<VALUE2>", str(element.children[1].children[1].value)) for elem in code.readlines()]
                                return snippet
                        elif element.children[0].fct == "Number" and element.children[1].children[1].fct == "Ident":
                            with open("assembly/snippets/soustraction.s", 'r') as code:
                                snippet = [elem.replace("<VALUE1>", str(element.children[0].value)).replace("<VALUE2>", "["+ str(element.children[1].children[1].value)+ "]") for elem in code.readlines()]
                                return snippet
                        else :
                            with open("assembly/snippets/soustraction.s", 'r') as code:
                                snippet = [elem.replace("<VALUE1>", str(element.children[0].value)).replace("<VALUE2>", str(element.children[1].children[1].value)) for elem in code.readlines()]
                                return snippet
                else : 
                    print("Opération non reconnue dans OPE5")
           
        #Si c'est une multiplication         
        elif element.fct == "OPE6" :
            if element.children[0].fct == "Number" or element.children[0].fct == "Ident":
                # Cas ou on a une multiplication de deux nombres ou deux variables
                if element.children[1].children[0].value == "*":
                    if element.children[1].children[1].fct == "Number" or element.children[1].children[1].fct == "Ident":
                        if element.children[0].fct == "Ident" and element.children[1].children[1].fct == "Ident":
                            with open("assembly/snippets/multiplication.s", 'r') as code:
                                snippet = [elem.replace("<VALUE1>", "["+str(element.children[0].value)+"]").replace("<VALUE2>", "["+str(element.children[1].children[1].value)+"]") for elem in code.readlines()]
                                return snippet
                        elif element.children[0].fct == "Ident" and element.children[1].children[1].fct == "Number":
                            with open("assembly/snippets/multiplication.s", 'r') as code:
                                snippet = [elem.replace("<VALUE1>", "["+str(element.children[0].value)+"]").replace("<VALUE2>", str(element.children[1].children[1].value)) for elem in code.readlines()]
                                return snippet
                        elif element.children[0].fct == "Number" and element.children[1].children[1].fct == "Ident":
                            with open("assembly/snippets/multiplication.s", 'r') as code:
                                snippet = [elem.replace("<VALUE1>", str(element.children[0].value)).replace("<VALUE2>", "["+ str(element.children[1].children[1].value)+ "]") for elem in code.readlines()]
                                return snippet
                        else :
                            with open("assembly/snippets/multiplication.s", 'r') as code:
                                snippet = [elem.replace("<VALUE1>", str(element.children[0].value)).replace("<VALUE2>", str(element.children[1].children[1].value)) for elem in code.readlines()]
                                return snippet
                elif element.children[1].children[0].value == "/":
                    if element.children[1].children[1].fct == "Number" or element.children[1].children[1].fct == "Ident":
                        if element.children[0].fct == "Ident" and element.children[1].children[1].fct == "Ident":
                            with open("assembly/snippets/division.s", 'r') as code:
                                snippet = [elem.replace("<VALUE1>", "["+str(element.children[0].value)+"]").replace("<VALUE2>", "["+str(element.children[1].children[1].value)+"]") for elem in code.readlines()]
                                return snippet
                        elif element.children[0].fct == "Ident" and element.children[1].children[1].fct == "Number":
                            with open("assembly/snippets/division.s", 'r') as code:
                                snippet = [elem.replace("<VALUE1>", "["+str(element.children[0].value)+"]").replace("<VALUE2>", str(element.children[1].children[1].value)) for elem in code.readlines()]
                                return snippet
                        elif element.children[0].fct == "Number" and element.children[1].children[1].fct == "Ident":
                            with open("assembly/snippets/division.s", 'r') as code:
                                snippet = [elem.replace("<VALUE1>", str(element.children[0].value)).replace("<VALUE2>", "["+ str(element.children[1].children[1].value)+ "]") for elem in code.readlines()]
                                return snippet
                        else :
                            with open("assembly/snippets/division.s", 'r') as code:
                                snippet = [elem.replace("<VALUE1>", str(element.children[0].value)).replace("<VALUE2>", str(element.children[1].children[1].value)) for elem in code.readlines()]
                                return snippet
                elif element.children[1].children[0].value == "rem":
                    if element.children[1].children[1].fct == "Number" or element.children[1].children[1].fct == "Ident":
                        if element.children[0].fct == "Ident" and element.children[1].children[1].fct == "Ident":
                            with open("assembly/snippets/rem.s", 'r') as code:
                                snippet = [elem.replace("<VALUE1>", "["+str(element.children[0].value)+"]").replace("<VALUE2>", "["+str(element.children[1].children[1].value)+"]") for elem in code.readlines()]
                                return snippet
                        elif element.children[0].fct == "Ident" and element.children[1].children[1].fct == "Number":
                            with open("assembly/snippets/rem.s", 'r') as code:
                                snippet = [elem.replace("<VALUE1>", "["+str(element.children[0].value)+"]").replace("<VALUE2>", str(element.children[1].children[1].value)) for elem in code.readlines()]
                                return snippet
                        elif element.children[0].fct == "Number" and element.children[1].children[1].fct == "Ident":
                            with open("assembly/snippets/rem.s", 'r') as code:
                                snippet = [elem.replace("<VALUE1>", str(element.children[0].value)).replace("<VALUE2>", "["+ str(element.children[1].children[1].value)+ "]") for elem in code.readlines()]
                                return snippet
                        else :
                            with open("assembly/snippets/rem.s", 'r') as code:
                                snippet = [elem.replace("<VALUE1>", str(element.children[0].value)).replace("<VALUE2>", str(element.children[1].children[1].value)) for elem in code.readlines()]
                                return snippet
                else:
                    print("Opération non reconnue dans OPE6")
            
    def add_if_loop(self, if_node):
        numero_bloc = self.blocks_number[0]

        self.blocks_number[0] += 1

        if if_node.children[1].children[0].value == ">":
            with open("assembly/snippets/comparaison_if.s") as code:
                snippet_condition = [element.replace("<VAR_1>", str(if_node.children[1].children[1].value)).replace("<VAR_2>", str(if_node.children[0].value)) for element in code]
        elif if_node.children[1].children[0].value == "<":
            with open("assembly/snippets/comparaison_if.s") as code:
                snippet_condition = [element.replace("<VAR_1>", str(if_node.children[0].value)).replace("<VAR_2>", str(if_node.children[1].children[1].value)) for element in code]
        elif if_node.children[1].children[0].value == "=":
            with open("assembly/snippets/comparaison_if.s") as code:
                snippet_condition = [element.replace("<VAR_1>", str(if_node.children[0].value)).replace("<VAR_2>", str(if_node.children[1].children[1].value)) for element in code]
        self.write_data([f"  call if_loop_{numero_bloc}\n\n"], self.current_placement)

        self.placement_history.append(self.current_placement)
        self.current_placement = f"  <FUNCTION_{self.blocks_number[3] - 1}_CODE>\n"

        with open("assembly/snippets/if_loop.s") as code:
            snippet = [element.replace("X", str(numero_bloc)).replace("  <IF_CODE>\n", ''.join(snippet_condition)) for element in code.readlines()]
        
        snippet = [element for element in snippet if element!="  <IF_CODE>\n"]

        self.write_data(snippet, self.current_placement)

        self.placement_history.append(self.current_placement)
        self.current_placement = f"  <IF_CODE_{numero_bloc}>\n"

    def add_return(self, variable):
        with open("assembly/snippets/return.s") as code:
            snippet = [element.replace("<RETURN_VAR>", variable) for element in code]
        self.write_data(snippet, self.current_placement)

    def initialize_variables(self, variables_liste):
        for element in variables_liste:
            #On vérifie si la valeur est un int (self.tds.tds_data[element].value.isdigit())
            if self.tds.tds_data[element].value == None:
                self.add_variable(self.tds.tds_data[element].name, None, self.tds.tds_data[element].type)
            elif type(self.tds.tds_data[element].value) == int:
                self.add_variable(self.tds.tds_data[element].name, self.tds.tds_data[element].value, self.tds.tds_data[element].type)     
            elif self.tds.tds_data[element].value.isdigit():
                self.add_variable(self.tds.tds_data[element].name, self.tds.tds_data[element].value, self.tds.tds_data[element].type)       
            else:
                self.add_variable(self.tds.tds_data[element].name, 0, self.tds.tds_data[element].type)

    def write_file(self):
        pattern = re.compile(r"  <FUNCTION_.*_CODE>\n")
        self.data = [element for element in self.data 
                     if ((element not in ["<DATA>\n", "<FUNCTIONS>\n", "<INSTRUCTIONS>\n", "  <FUNCTION_CODE>\n"]) 
                         and ("FOR_LOOP_CODE_" not in element) 
                         and ("IF_CODE" not in element) 
                         and ("IF_TRUE_CODE" not in element) 
                         and ("IF_FALSE_CODE" not in element) 
                         and ("INSTRUCTION_BOUCLE" not in element))
                         and not pattern.match(element)]
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

        if self.writing_flags[5] == 1:
            if element.fct == "Keyword" and element.value == "return":
                self.writing_flags[5] = 2 

        if self.writing_flags[5] == 2:
            if element.fct == "Ident":
                self.add_return(element.value)
                self.writing_flags[5] = 0

        if self.writing_flags[6] == 1:
            if element.fct[:-1] == "OPE":
                self.add_if_loop(element)
                self.writing_flags[6] = 0
            self.writing_flags[6] = 0

        if element.children!=[]:
            if element.children[0].value == "put":
                print("put statement")
                global cunt_put
                cunt_put +=1
                if element.children[1].fct == "Ident":
                    self.add_put_var(self.tds.tds_data[element.children[1].value], cunt_put)
                elif element.children[1].fct == "Number":
                    self.add_put_cst(element.children[1].value, cunt_put)

        if element.fct=="Keyword":
            if element.value == "procedure":
                self.writing_flags[0] = 1
                return
            elif element.value =="function":
                self.writing_flags[1] = 1
                return
            elif element.value == "end":
                self.current_placement = self.placement_history[-1]
                self.placement_history.pop()
                self.writing_flags[4] = 0
                if self.is_writing_function:
                    self.is_writing_function = 0
                    self.data = [element for element in self.data if f"<FUNCTION_{self.blocks_number[3]}_CODE>" not in element]
            elif element.value == "then":
                current_if_block = self.blocks_number[0]-1
                self.current_placement = f"  <IF_TRUE_CODE_{current_if_block}>\n"
            elif element.value == "else":
                current_if_block = self.blocks_number[0]-1
                self.current_placement = f"  <IF_FALSE_CODE_{current_if_block}>\n"
            elif element.value == "return":
                if self.writing_flags[5] == 0:
                    self.writing_flags[5] = 1 
            elif element.value == "if":
                self.writing_flags[6] = 1


        if element.fct== "Ident":
            if element.value not in self.generated:
                pass
        if element.fct == "INSTR":
            if element.children[0].fct == "Ident":
                if element.children[1].value == ":=":
                    if element.children[2].fct[:3] == "OPE" and element.children[2].value == None:
                        snip = self.operation(element.children[2])
                        snippet = [elem.replace("<RESULT>", str(element.children[0].value)) for elem in snip]
                        self.write_data(snippet, self.current_placement)
                        element.children[2].value = 1
                    else:
                        self.add_assignation(element.children[0].value, str(element.children[2].value))
                    # on print l'assignation
                    #print(f"{element.children[0].value} := {element.children[2].value}") ##########################################################
                    pass
                    # calculer membre de droite
                    # assigner valeur dans membre de gauche
            elif element.children[0].fct == "Keyword":
                if element.children[0].value == "while":
                    print("while loop")
                elif element.children[0].value == "for":
                    self.add_for_loop(element)
                    
        if element.fct[:3] == "OPE" and element.value == None:
            self.operation(element)

    def dfs(self, node):
        self.write_assembly(node)

        for child in node.children:
            if child not in self.dfs_history:
                self.dfs(child)
                self.dfs_history.append(child)

if __name__ == "__main__":
    gene = assembly_generator()
