import os
import sys

class assembly_generator:

    def __init__(self):
        if os.path.exists("asm_output"):
            pass
        else:
            os.mkdir("asm_output")
        
        if os.path.exists("asm_output/output.s"):
            sys.stdout.write("[!] Attention! Un fichier 'output.s' est déjà présent dans le répertoire 'asm_output'.\n\tVoulez-vous tout de même lancer la génération de code assembleur?\n\tNOTE: Cela écrasera les données pré-existantes\n")
            self.file_exists()
        with open("assembly/program_template/program_template.s", "r") as file:
            self.data = file.readlines()
        self.line_index = 0  
        self.add_function("test")
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
            file_exists()


    def add_function(self, function_name):
        pass
        #Bonne chance hein

    def add_procedure(self, procedure_name):
        pass

    def write_file(self):
        with open("asm_output/output.s", "a") as file:
            for line in self.data:
                file.write(line)

if __name__ == "__main__":
    gene = assembly_generator()
