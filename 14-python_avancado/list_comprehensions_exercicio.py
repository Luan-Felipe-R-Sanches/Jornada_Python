# Cria uma lista chamada 'resultado' com números de 0 a 500 que são múltiplos de 4 e 5
resultado = [numero for numero in range(0, 501) if numero % 4 == 0 if numero % 5 == 0]

# Imprime os números que satisfazem as condições (múltiplos de 4 e 5)
print(resultado)
