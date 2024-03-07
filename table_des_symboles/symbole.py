import sys


class variable:

    def __init__(self, name, type_entree="None", mode="in", value = None, size=0, Dimension=0, ligne_declaration=None, ligne_utilisation=None, address=None):
        self.name = name
        self.type = type_entree
        self.value = value
        self.size = size
        self.Dimension = Dimension
        self.ligne_declaration = ligne_declaration
        self.ligne_utilisation  = ligne_utilisation
        self.address = address
        self.mode = mode

    def __repr__(self):
        repr = ""
        repr += f"variable(self.name)"
        return repr
        """
        sys.stdout.write("\t\tType: " + str(self.type_entree))
        sys.stdout.write("\t\tTaille: " + str(self.Dimension))
        sys.stdout.write("\t\tDimension: " + str(self.ligne_declaration))
        sys.stdout.write("\t\tLigne de déclaration: " + self.name)
        utilisation_str = ""
        if len(self.ligne_utilisation)>1:
            for ligne in self.ligne_utilisation:
                utilisation_str += ligne
            sys.stdout.write("\t\tLignes d'utilisation: " + str(utilisation_str))
        sys.stdout.write("\t\tLigne d'utilisation: " + str(self.ligne_utilisation[0]))
        sys.stdout.write("Adresse mémoire: " + str(self.address))
        """

class fonction:

    def __init__(self, name, parametres = {}, type_de_retour = None, size=0, Dimension=0, ligne_declaration=None, ligne_utilisation=None, address=None):
        self.name = name
        self.parametres = parametres
        self.type_de_retour = type_de_retour
        self.size = size
        self.Dimension = Dimension
        self.ligne_declaration = ligne_declaration
        self.ligne_utilisation  = ligne_utilisation
        self.address = address
        self.sous_bloc = None

    def __repr__(self):
        return "function name:  " + self.name

    def __str__(self):
        repr=""
        repr+=f"fonction({self.name}): {self.sous_bloc.__repr__()}"
        return repr
        """
        if len(self.parametres)>1:
            parametres_str = ""
            for element in self.parametres:
                parametres_str+= (self.parametres + ", ")
        sys.stdout.write("\t\tParamètres: " + parametres_str)
        sys.stdout.write('Retour: ' + self.retour)
        sys.stdout.write("\t\tTaille: " + str(self.Dimension))
        sys.stdout.write("\t\tDimension: " + str(self.ligne_declaration))
        sys.stdout.write("\t\tLigne de déclaration: " + self.name)
        utilisation_str = ""
        if len(self.ligne_utilisation)>1:
            for ligne in self.ligne_utilisation:
                utilisation_str += ligne
            sys.stdout.write("\t\tLignes d'utilisation: " + str(utilisation_str))
        sys.stdout.write("\t\tLigne d'utilisation: " + str(self.ligne_utilisation[0]))
        sys.stdout.write("Adresse mémoire: " + str(self.address))
        """

class procedure:

    def __init__(self, name, parametres = {}, size=0, Dimension=0, ligne_declaration=None, ligne_utilisation=None, address=None):
        self.name = name
        self.parametres = parametres
        self.size = size
        self.Dimension = Dimension                                     
        self.ligne_declaration = ligne_declaration
        self.ligne_utilisation  = ligne_utilisation
        self.address = address
        self.sous_bloc = None

    def __repr__(self):
        repr="" 
        repr+=f"procedure({self.name}) : self.{sous_bloc}"
        sys.stdout.write("\n\t => PROCEDURE\n")
        sys.stdout.write("\t\tNom: " + str(self.name))
        if len(self.parametres)>1:
            parametres_str = ""
            for element in self.parametres:
                parametres_str+= (self.parametres + ", ")
        sys.stdout.write("\t\tParamètres: " + parametres_str)
        sys.stdout.write("\t\tTaille: " + str(self.Dimension))
        sys.stdout.write("\t\tDimension: " + str(self.ligne_declaration))
        sys.stdout.write("\t\tLigne de déclaration: " + self.name)
        utilisation_str = ""
        if len(self.ligne_utilisation)>1:
            for ligne in self.ligne_utilisation:
                utilisation_str += ligne
            sys.stdout.write("\t\tLignes d'utilisation: " + str(utilisation_str))
        sys.stdout.write("\t\tLigne d'utilisation: " + str(self.ligne_utilisation[0]))
        sys.stdout.write("Adresse mémoire: " + str(self.address))
