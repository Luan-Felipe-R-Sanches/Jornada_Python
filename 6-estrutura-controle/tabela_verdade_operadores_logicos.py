# Tabela Verdade para os Operadores Lógicos em Python

# Tabela verdade para o operador 'and'
print("Tabela Verdade para 'and':")
print("A      B      A and B")
print("-----------------------")
print("True   True   ", True and True)     # Retorna True apenas se ambos os operandos forem True
print("True   False  ", True and False)    # Retorna False se pelo menos um dos operandos for False
print("False  True   ", False and True)    # Retorna False se pelo menos um dos operandos for False
print("False  False  ", False and False)   # Retorna False se pelo menos um dos operandos for False

# Tabela verdade para o operador 'or'
print("\nTabela Verdade para 'or':")
print("A      B      A or B")
print("----------------------")
print("True   True   ", True or True)       # Retorna True se pelo menos um dos operandos for True
print("True   False  ", True or False)      # Retorna True se pelo menos um dos operandos for True
print("False  True   ", False or True)      # Retorna True se pelo menos um dos operandos for True
print("False  False  ", False or False)     # Retorna False apenas se ambos os operandos forem False

# Tabela verdade para o operador 'not'
print("\nTabela Verdade para 'not':")
print("A      not A")
print("--------------")
print("True   ", not True)    # Retorna False ao inverter True
print("False  ", not False)   # Retorna True ao inverter False
