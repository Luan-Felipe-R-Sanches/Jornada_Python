# Faça um programa que peça um número inteiro e determine se ele é primo
# ou não.

numero = int(input("Digite um número inteiro: "))

# Verifica se o número é menor ou igual a 1, pois números menores que 2 não são primos
if numero <= 1:
    print("O número não é primo.")
else:
    primo = True  # Assumimos inicialmente que o número é primo
    for i in range(2, numero):  # Verifica divisibilidade do número por todos os números de 2 até o número - 1
        if numero % i == 0:  # Se o resto da divisão for zero, o número não é primo
            primo = False
            break  # Se encontramos um divisor, não é mais necessário continuar verificando
    if primo:
        print("O número é primo.")
    else:
        print("O número não é primo.")
