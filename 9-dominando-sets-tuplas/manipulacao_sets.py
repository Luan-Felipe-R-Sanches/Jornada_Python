# Cria um conjunto 's' com os elementos 1, 2 e 3
s = {1, 2, 3}

# Adiciona o elemento 4 ao conjunto 's'
s.add(4)
print(s)  # Resultado: {1, 2, 3, 4}

# Remove o elemento 2 do conjunto 's'
s.remove(2)
print(s)  # Resultado: {1, 3, 4}

# Descarta o elemento 3 do conjunto 's'. Este método não lança um erro se o elemento não existir no conjunto
s.discard(3)
print(s)  # Resultado: {1, 4}

# Remove e retorna um elemento aleatório do conjunto 's'
x = s.pop()
print(x)  # Resultado: 1 (pode variar)
print(s)  # Resultado: {4} (pode variar)

# Cria dois novos conjuntos 's1' e 's2'
s1 = {1, 2, 3}
s2 = {3, 4, 5}

# Cria um novo conjunto 's3' que é a união dos conjuntos 's1' e 's2'
s3 = s1.union(s2)
print(s3)  # Resultado: {1, 2, 3, 4, 5}

# Cria um novo conjunto 's4' que é a intersecção dos conjuntos 's1' e 's2'
s4 = s1.intersection(s2)
print(s4)  # Resultado: {3}

# Cria um novo conjunto 's5' que é a diferença entre os conjuntos 's1' e 's2'
s5 = s1.difference(s2)
print(s5)  # Resultado: {1, 2}
