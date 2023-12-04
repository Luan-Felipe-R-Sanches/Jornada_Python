# Função copy()

# Dicionário original
original = {'a': 1, 'b': 2, 'c': [3, 4, 5]}

# Criando uma cópia superficial
copia = original.copy()

# Adicionando um elemento na lista 'c' da cópia
copia['c'].append(6)

# Imprimindo os resultados
print("Original:", original)  # Mostra o dicionário original
print("Cópia:", copia)  # Mostra a cópia com a lista modificada

# Método items()

dicionario = {'a': 1, 'b': 2, 'c': 3}

# Usando items() para obter pares chave-valor
for chave, valor in dicionario.items():
    print(f"Chave: {chave}, Valor: {valor}")  # Mostra cada chave e valor no dicionário

# Método keys()

dicionario = {'a': 1, 'b': 2, 'c': 3}

# Obtendo todas as chaves usando keys()
todas_as_chaves = dicionario.keys()

print("Chaves:", todas_as_chaves)  # Mostra as chaves do dicionário

# Método setdefault()

dicionario = {'a': 1, 'b': 2}

# Usando setdefault() para 'c', que não existe
valor = dicionario.setdefault('c', 3)

# Imprimindo os resultados
print("Dicionário:", dicionario)  # Mostra o dicionário com 'c' adicionado
print("Valor de 'c':", valor)  # Mostra o valor associado à chave 'c'


# Método fromkeys()

# Criando um dicionário com chaves definidas e valores padrão
chaves = ['a', 'b', 'c']
valor_padrao = 0

# Usando fromkeys() para criar um dicionário com chaves e valores padrão
novo_dicionario = dict.fromkeys(chaves, valor_padrao)

print("Novo Dicionário:", novo_dicionario)  # Mostra o dicionário criado com as chaves e valores padrão
