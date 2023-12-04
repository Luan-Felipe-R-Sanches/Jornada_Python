#  Faça um programa que peça ao usuário para digitar 10 números e exiba a
# soma deles

soma = 0

for i in range(10):
    numero = float(input(f"Digite o número {i + 1}/10: "))
    soma += numero

print(f"A soma dos 10 números é: {soma}")
