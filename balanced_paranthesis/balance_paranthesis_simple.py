def paren_checker(string):
    counter = 0
    for c in string:
        if c == '(' or '{' or '[':
            counter += 1
        elif c == ')'or '}'or ']':
            counter -= 1
        if counter < 0:
            return False

    if counter == 0:
        return True
    return False


string = "((){}){"
print(paren_checker(string))
