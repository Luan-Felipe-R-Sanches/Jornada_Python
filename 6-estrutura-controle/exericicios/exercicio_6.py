# Escreva um programa que imprima a tabuada de um número informado
# pelo usuário

numero = int(input("Insira um número: "))
for i in range(1, 11):
    resultado = numero * i;
    print(f'{numero}  X  {i} = {resultado}')
