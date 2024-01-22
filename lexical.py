import re

def splitTokens(filePath):
    with open(filePath, 'r') as file:
        code = file.read()

    tokens = re.findall(r'[a-zA-Z_]\w*|[-+*/<>=]|[.,;{}\[\]()]', code)

    for token in tokens:
        if token in ['+', '-', '*', '/', '<', '>', '=']:
            print(f"{token} is an Operator")
        elif token in [',', ';', '[', ']', '{', '}', '(', ')']:
            print(f"{token} is a Delimiter")
        elif token in ['int', 'float', 'char', 'double', 'if', 'else', 'for', 'while']:
            print(f"{token} is a Keyword")
        elif re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token):
            print(f"{token} is an Identifier")
        else:
            print(f"{token} is a Constant")

filePath = 'bello.c'
splitTokens(filePath)