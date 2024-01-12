import lexeur.lexeur as lex
import parseur.parseur as parse

from parseur.table_syntaxique import table_syntaxique as table_ll1




def print_tokens(tokens):
    current_line = tokens[0][2]

    for _, (token_type, token_value, token_line) in enumerate(tokens):
        if token_line != current_line:
            print()
            current_line = token_line

        print(f"<{token_type}, {token_value}>", end=' ')
        
        

def print_explicit_tokens(tokens, list_type_token, lexical_table):
    current_line = tokens[0][2]

    for _, (token_type, token_value, token_line) in enumerate(tokens):
        if token_line != current_line:
            print()
            current_line = token_line
        if token_type == 4:
            print(f"<{list_type_token[token_type]}, {token_value}>", end=' ')
        else:
            print(f"<{list_type_token[token_type]}, {lexical_table[token_type][token_value]}>", end=' ')


list_type_token = {
        0: "Keyword",
        1: "Operator",
        2: "Syntax Operator",
        3: "Identifier",
        4: "Constant Number",
        5: "Invalid Character"
    }


def test_parseur(filename, output_filename):
    with open(filename, 'r') as file:
        source_code = file.read()

    #On lance l'analyse lexicale
    tokens, lexical_table = lex.lexical_analysis(source_code)
    
    
    # Enregistrement de la liste de tokens et de la table lexicale dans un fichier
    with open(output_filename, 'w') as output_file:
        # Écriture de la liste de tokens
        output_file.write("Liste des tokens :\n")
        for token in tokens:
            output_file.write(str(token) + '\n')

        # Écriture de la table lexicale
        output_file.write("\nTable Lexicale :\n")
        for key, values in lexical_table.items():
            output_file.write(f"{list_type_token[key]}: {values}\n")

    
    print("\n \nTable Lexicale:")
    for key, values in lexical_table.items():
        print(f"    {list_type_token[key]}: {values}")
    print(f"\n\nListe des tokens pour {filename} avec les tokens de la forme <type, valeur>: \n")
    
    
    #version tokens explicites
    print_explicit_tokens(tokens, list_type_token, lexical_table)
    
    #version tokens brutes
    print("\n\n\n\nListe brutes des tokens: \n")
    print_tokens(tokens)

    
    #On fait à présent l'analyse syntaxique
    print("\n\n\n\nAnalyse syntaxique: \n")
    resultat_parseur = parse.parse(tokens, lexical_table, table_ll1)
    if resultat_parseur:
        print("L'analyse syntaxique a réussi sans erreur")
    else:
        print("L'analyse syntaxique a échoué")
    

    print("\n")


#Test qui fonctionne bien
#test_lexeur('test_lexeur/test1.txt')

#Test avec utilisation d'un caractère interdit:
test_parseur('tests/test_lexeur/test1.txt', 'tests/test_lexeur/output_test1.txt')

#Test avec utilisation d'un rem sans espace:
#test_lexeur('test_lexeur/test3.txt')

#Test avec utilisation d'un identifiant commençant par un chiffre:
#test_lexeur('test_lexeur/test4.txt')

#Test avec plusieurs erreurs:
#test_lexeur('test_lexeur/test5.txt')