# Cria dois conjuntos 's1' e 's2'
s1 = {1, 2, 3}
s2 = {3, 4, 5}

# União: Cria um novo conjunto 's_union' que é a união dos conjuntos 's1' e 's2' (todos os elementos que estão em 's1' ou 's2')
s_union = s1 | s2
print(s_union)  # Resultado: {1, 2, 3, 4, 5}

# Intersecção: Cria um novo conjunto 's_intersection' que é a intersecção dos conjuntos 's1' e 's2' (todos os elementos que estão em 's1' e 's2')
s_intersection = s1 & s2
print(s_intersection)  # Resultado: {3}

# Diferença: Cria um novo conjunto 's_difference' que é a diferença entre os conjuntos 's1' e 's2' (todos os elementos que estão em 's1', mas não em 's2')
s_difference = s1 - s2
print(s_difference)  # Resultado: {1, 2}

# Diferença simétrica: Cria um novo conjunto 's_sym_difference' que é a diferença simétrica entre os conjuntos 's1' e 's2' (todos os elementos que estão em 's1' ou 's2', mas não em ambos)
s_sym_difference = s1 ^ s2
print(s_sym_difference)  # Resultado: {1, 2, 4, 5}