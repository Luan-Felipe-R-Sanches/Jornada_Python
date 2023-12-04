# Escreva um programa que calcule o fatorial de um número.

numero = int(input("Digite um número inteiro: "))

if numero < 0:
    print("O fatorial não está definido para números negativos.")
elif numero == 0 or numero == 1:
    print(f"O fatorial de {numero} é 1.")
else:
    fatorial = 1
    for i in range(2, numero + 1):
        fatorial *= i
    print(f"O fatorial de {numero} é {fatorial}.")
