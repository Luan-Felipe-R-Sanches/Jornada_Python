# Escreva um programa que solicite ao usuário que adivinhe um número que
# está entre 1 e 100. O programa deve fornecer dicas ao usuário, informando se o número
# a ser encontrado é maior ou menor do que a tentativa informada.

import random

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número entre 1 e 100.")

while True:
    tentativa = int(input("Digite o seu palpite: "))

    if tentativa < numero_secreto:
        print("Tente um número maior.")
    elif tentativa > numero_secreto:
        print("Tente um número menor.")
    else:
        print("Parabéns! Você acertou!")
        break
