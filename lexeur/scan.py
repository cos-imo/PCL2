mots_cles = [
    "access", "and", "begin", "else", "elsif", "end", "false", "for", "function", "if", "in", "is", "loop", "new", "not", "null", "or", "out", "procedure", "record", "rem", "return", "reverse", "then", "true", "type", "use", "while", "with"
]


#Classe StringTab qui contient une chaine de caractère et lui associe son token
class StringTable:
    def __init__(self):
        self.mapping = {}  # Un dictionnaire pour stocker les associations chaîne de caractères -> token

    def add_string(self, chaine, token):
        # Ajouter une association chaine -> token à la table
        self.mapping[chaine] = token

    def get_token(self, chaine):
        # Obtenir le token associé à une chaîne donnée, ou None si la chaîne n'est pas présente dans la table
        return self.mapping.get(chaine)


st = StringTable()
#On ajoute les mots clés dans notre table
for mot_cle in mots_cles:
    st.add_string(mot_cle, f"<{mot_cle}>")
    





#Fonction qui permet de passer les espaces et les retours à la ligne
def skip_whitespace(source_code, position,ligne):
    while position < len(source_code) and (source_code[position] == ' ' or source_code[position] == '\n'):
        if source_code[position]=='\n':
            ligne+=1
            position+=1
        elif source_code[position] == ' ':
            position += 1
        
    return position


#Fonction qui permet de scanner les nombres
def scan_number(source_code, position):
    v= 0
    while position < len(source_code) and source_code[position].isdigit():
        v= v*10 + int(source_code[position])
        position += 1
    return position, v



#Fonction qui permet de scanner les identifiants ou les mots clés
def scan_identifier(source_code, position):
    buffer = ''
    while position < len(source_code) and  (source_code[position].isalpha() or source_code[position].isdigit() or source_code[position] == '_') :
        buffer += source_code[position]
        position += 1
    if st.get_token(buffer) != None:
        return position, st.get_token(buffer)
    else:
        st.add_string(buffer, f"<id, {buffer}>")
        return position, f"<id, {buffer}>"




#Fonction principale qui permet de scanner le code source
def scan(source_code):
    position = 0
    tokens = []
    peek = 1
    ligne=1

    while position < len(source_code):
        #On saute les espaces et les retours à la ligne
        position = skip_whitespace(source_code, position, ligne)
        

        #Identifier des nombres
        if position < len(source_code) and source_code[position].isdigit():
            position, token = scan_number(source_code, position)
            tokens.append(f"<num,{token}>")

        #Identifier des identifiants ou des mots clés
        elif position < len(source_code) and source_code[position].isalpha():
            position, token = scan_identifier(source_code, position)
            tokens.append(token)

        #Identifier ici les symboles restants:
        else:
            tokens.append((source_code[position],))
            print("problème: " , source_code[position])
            position += 1

    return tokens






#Programme principale

#Récupération du fichier code source
source_code = open("code.txt", "r").read()
#source_code = "Bonjour je suis un arbre de 15 metres de haut"

#Création de la liste des tokens
tokens = scan(source_code)


# Affichage des tokens
for token in tokens:

    print(token)
    
#Affichage de la table de string
print("Affichage de la table de string:")
print(st.mapping)

