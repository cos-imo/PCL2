import os
import sys

class assembly_generator:

    def __init__(self, arbre):
        """
        Variable contenant le numéro de ligne (du fichier assembleur) actuel
            0: ligne data
            1: ligne instruction
        """
        self.line_index = [0 for i in range (2)]  

        # Dictionnaire contenant les addresses des variables, de la forme {'nom_de_la_variable': 'addresse'}
        self.variables_addresses = {}

        self.arbre = arbre

        print(self.arbre)

        ### Création du fichier de code assembleur
        ## Création du dossier s'il n'existe pas déjà au préalable
        if os.path.exists("asm_output"):
            pass
        else:
            os.mkdir("asm_output")

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

    def add_var(self, var_type, var_name):
        pass

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
        function = [f"{function_name}:"]
        #function_data = self.tds.tds_data[function_name]
        function.append("\tpushl %ebp")
        function.append("\tmovl %esp %ebp")
        self.data = self.data[:self.line_index] + function + self.data[self.line_index:]
        pass
        #Bonne chance hein

    def add_procedure(self, procedure_name):
        pass

    def add_variable(self, variable_name, variable_value, variable_type):
        if variable_type == "string":
            declaration = "\t.asciz " + variable_value
        self.data = self.data[:self.line_index[0]] + declaration + self.data[self.line_index[0]:]
        for i in range(len(line_index)):
            self.line_index[i]+=1

    def update_line_index(self, offset):
        pass

    def write_file(self):
        with open("asm_output/output.s", "a") as file:
            for line in self.data:
                file.write(line)

    def generate_assembly(self):
        self.dfs(self.arbre)

    def write_assembly(self, element):
        flags= [0, 0, 0, 0] # flag 0: function, flag 1: procedure, flag2: variable, flag3: Ident
        if any(flags):
            if flags[0]:
               pass 
            elif flags[1]:
               pass
            elif flags[2]:
               variable_data = self.tds[element.value]
               pass
        else:
            if element.value == "procedure":
                flags = [0 for i in range(4)]
                flags[1] = 1
            elif element.value == "function":
                flags = [0 for i in range(4)]
                flags[0] = 1
            elif element.value in ["integer"]: # Rajouter tout les types de variables dispo instruction
                flags = [0 for i in range(4)]
                flags[2] = 1

    def dfs(self, currentNode):
        self.write_assembly(currentNode)
        if currentNode.children:
            for child in currentNode.children:
                self.write_assembly(child)

    def append_uniq(self, element, liste):
        liste.append(element)
        liste = list(set(liste))

if __name__ == "__main__":
    gene = assembly_generator()
