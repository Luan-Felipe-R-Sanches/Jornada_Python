#  Crie um programa que leia uma expressão matemática e verifica se os
# parênteses estão balanceados.

expressao = input("Digite uma expressão matemática: ")
pilha = []

for char in expressao:
    if char == "(":
        pilha.append(char)
    elif char == ")":
        if len(pilha) == 0:
            pilha.append(char)
            break
        pilha.pop()

if len(pilha) == 0:
    print("Os parênteses estão balanceados.")
else:
    print("Os parênteses não estão balanceados.")
