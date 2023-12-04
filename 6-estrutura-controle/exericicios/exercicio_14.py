#  Faça um programa que mostre na tela a sequência de Fibonacci até um
# determinado número informado pelo usuário.

limite = int(input("Digite um número limite para a sequência de Fibonacci: "))

# Inicializa os dois primeiros números da sequência
a, b = 0, 1
fibonacci = []

# Adiciona os números à lista até atingir o limite
while a <= limite:
    fibonacci.append(a)
    a, b = b, a + b

print("Sequência de Fibonacci até", limite, ":", fibonacci)
