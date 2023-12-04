# Escreva um programa que verifique se uma palavra é um pangrama (frase
# que usa todas as letras do alfabeto pelo menos uma vez).
frase = input("Informe uma frase: ").lower()
letras = set()

for letra in frase:
    if letra.isalpha():
        letras.add(letra)

if len(letras) == 26:
    print("A frase é um pangrama.")
else:
    print("A frase não é um pangrama.")
