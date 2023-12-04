
# Criando uma lista
lista = [1, 2, 3, 4]

# Adicionando um elemento no final da lista
lista.append(5)
print(lista)  # [1, 2, 3, 4, 5]

# Adicionando vários elementos ao final da lista
lista.extend([6, 7, 8])
print(lista)  # [1, 2, 3, 4, 5, 6, 7, 8]

# Adicionando um elemento em uma posição específica da lista
lista.insert(2, 10)
print(lista)  # [1, 2, 10, 3, 4, 5, 6, 7, 8]

# Removendo um elemento específico da lista
lista.remove(5)
print(lista)  # [1, 2, 10, 3, 4, 6, 7, 8]

# Removendo o último elemento da lista e o retornando
ultimo_elemento = lista.pop()
print(ultimo_elemento)  # 8
print(lista)  # [1, 2, 10, 3, 4, 6, 7]

# Retornando o índice da primeira ocorrência de um elemento específico na lista
indice = lista.index(3)
print(indice)  # 3

# Retornando o número de ocorrências de um elemento específico na lista
ocorrencias = lista.count(6)
print(ocorrencias)  # 1

# Ordenando a lista em ordem crescente
lista.sort()
print(lista)  # [1, 2, 3, 4, 6, 7, 10]

# Invertendo a ordem dos elementos da lista
lista.reverse()
print(lista)  # [10, 7, 6, 4, 3, 2, 1]
