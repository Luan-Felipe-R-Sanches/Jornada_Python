# Criação de uma tupla
tupla = (1, 2, 3, 4, 5)
print(tupla)  # Resultado: (1, 2, 3, 4, 5)

# Acessando elementos em uma tupla
primeiro_elemento = tupla[0]
print(primeiro_elemento)  # Resultado: 1

# Fatia de uma tupla
fatia_tupla = tupla[1:3]
print(fatia_tupla)  # Resultado: (2, 3)

# Concatenação de tuplas
tupla2 = (6, 7, 8)
tupla_concatenada = tupla + tupla2
print(tupla_concatenada)  # Resultado: (1, 2, 3, 4, 5, 6, 7, 8)

# Contando o número de ocorrências de um elemento
contagem = tupla.count(2)
print(contagem)  # Resultado: 1

# Encontrando o índice de um elemento
indice = tupla.index(3)
print(indice)  # Resultado: 2

# Verificando o comprimento de uma tupla
comprimento = len(tupla)
print(comprimento)  # Resultado: 5

# Tupla com elementos de tipos diferentes
tupla_mista = (1, "dois", 3.0, [4, 5], (6, 7))
print(tupla_mista)  # Resultado: (1, 'dois', 3.0, [4, 5], (6, 7))
