import sys

class symbole:

    def __init__(self, name, type_entree="None", value = None, size=0, Dimension=0, ligne_declaration=None, ligne_utilisation=None, address=None):
        self.name = name
        self.type = type_entree
        self.value = value
        self.size = size
        self.Dimension = Dimension
        self.ligne_declaration = ligne_declaration
        self.ligne_utilisation  = ligne_utilisation
        self.address = address

    def __repr__(self):
        sys.stdout.write("\t => SYMBOLE\n")
        sys.stdout.write("\t\tNom: " + str(self.name))
        sys.stdout.write("\t\tType: " + str(self.type_entree))
        sys.stdout.write("\t\tTaille: " + str(self.Dimension))
        sys.stdout.write("\t\tDimension: " + str(self.ligne_declaration))
        sys.stdout.write("\t\tLigne de déclaration: " + self.name)
        utilisation_str = ""
        if len(ligne_utilisation)>1:
            for ligne in ligne_utilisation:
                utilisation_str += ligne
            sys.stdout.write("\t\tLignes d'utilisation: " + str(utilisation_str))
        sys.stdout.write("\t\tLigne d'utilisation: " + str(ligne_utilisation[0]))
        sys.stdout.write("Adresse mémoire: " + str(address))
