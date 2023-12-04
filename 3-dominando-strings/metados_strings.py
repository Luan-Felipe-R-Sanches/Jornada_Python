# Remove espaços em branco no início e fim da string
print('   Strip    '.strip())

# Converte a string para letras maiúsculas
print('maiúsculo'.upper())

# Converte a string para letras minúsculas
print('MINÚSCULO'.lower())

# Remove todas as vírgulas da string
print('T,exto, c,o,m vá,ria,s v,ír,g,ulas'.replace(',', ''))

# Conta quantas vezes o caractere 'e' aparece na string
print('Texto teste para função count'.count('e'))

# Centraliza a string em uma string de tamanho 50 preenchida com '*'
print('Texto Centralizado'.center(50, '*'))

# Retorna o índice da primeira ocorrência do caractere 'ã'
print('Avião?'.index('ã'))

# Verifica se a string é numérica
print('Alfanumérico'.isnumeric())

# Divide a string em uma lista separada por espaços
print('Teste de quebra de string com split'.split(' '))

# Divide a string em uma lista usando espaços como separador (padrão)
print('NOME;CIDADE;IDADE;PAÍS'.split())

# Converte a string para o formato de título
print('este é um título'.title())

# Converte apenas o primeiro caractere da string para maiúsculo
print('este é um título'.capitalize())

# Preenche a string com zeros à esquerda até atingir o comprimento especificado (5 caracteres)
print('585'.zfill(5))

# Encadeamento de Funções:
# Remove ponto e vírgula, divide a string em uma lista, junta os elementos dessa lista separados por um espaço,
# centraliza o texto, e converte para letras maiúsculas.
print(' Te;x;;to     '.replace(';', '').split(), ' '.join(' Te;x;;to     '.replace(';', '').split()).center(25, '*').upper())

# Tamanho de Strings:
# Retorna o número de caracteres na string
print(len('Essa é uma string extensa. como faremos para saber o tamanho?'))
