# Crie um programa que verifique se uma string é um palíndromo (inverso de
# outra, como “ovo” e “arara”).

string = input("Insira uma string: ")
string_inversa = string[::-1]

if string == string_inversa:
    print(string, "é um palíndromo!")
else:
    print(string, "não é um palíndromo.")

