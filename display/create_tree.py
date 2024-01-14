from parseur.ast_pars import est_terminal


def create_tree(rules):
    """
    return the ast for a program
    :param rules: the grammar rule
    :return: a dict constituting the ast
    """
    ast = {rules[0][0]: []}
    queue = [rules[0][0]]

    for i in range(len(rules)):
        current = queue.pop(0)

        if est_terminal(current):
            ast.update({current: rules[i][1]})
        else:
            print(i, rules[i])

            if current not in ast:
                ast.update({current: []})

            for j in range(len(rules[i][1])):
                ast[current].append(rules[i][1][j])

                queue.append(rules[i][1][j])

    return ast
