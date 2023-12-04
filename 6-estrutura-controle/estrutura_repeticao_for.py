# For: Sintaxe básica

# Definição de uma lista
sequencia = [1, 2, 3]

# Loop for que itera sobre os elementos da lista 'sequencia'
for elemento in sequencia:
    print(f'{elemento}')  # Imprime cada elemento da lista

# Range

# Loop for utilizando a função range
# O range cria uma sequência de números de acordo com os parâmetros fornecidos
# No exemplo, range(0, 10, 2) cria uma sequência começando em 0 (incluído), indo até 10 (excluído), com um passo de 2
for i in range(0, 10, 2):
    print(f'O valor de i é: {i}')  # Imprime o valor atual de 'i' durante cada iteração do loop


# Lista:
lista = [1, 2, 3, 4, 5]

print("Iterando por uma lista:")
for elemento in lista:
    print(elemento)

# Dicionário:
dicionario = {'a': 1, 'b': 2, 'c': 3}

print("\nIterando por um dicionário - chaves:")
for chave in dicionario:
    print(chave)

print("\nIterando por um dicionário - valores:")
for valor in dicionario.values():
    print(valor)

print("\nIterando por um dicionário - chaves e valores:")
for chave, valor in dicionario.items():
    print(f'Chave: {chave}, Valor: {valor}')

# Conjunto (Set):
conjunto = {1, 2, 3, 4, 5}

print("\nIterando por um conjunto:")
for elemento in conjunto:
    print(elemento)

# Tupla:
tupla = (1, 2, 3, 4, 5)

print("\nIterando por uma tupla:")
for elemento in tupla:
    print(elemento)
