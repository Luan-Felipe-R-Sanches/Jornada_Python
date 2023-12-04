# Crie um programa que peça um tamanho e crie uma lista com esse
# tamanho, preenchendo-a com números informados pelo usuário.

tamanho = int(input("Digite o tamanho da lista: "))
nova_lista = []

for i in range(tamanho):
    numero = int(input(f"Digite o número {i + 1}/{tamanho}: "))
    nova_lista.append(numero)

print("Lista criada:", nova_lista)

