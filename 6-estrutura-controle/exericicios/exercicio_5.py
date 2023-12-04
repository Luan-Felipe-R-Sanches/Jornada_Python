# Crie um programa que imprima todos os números de 1 até 100, substituindo
# os múltiplos de 3 pela palavra “Fizz” e os múltiplos de 5 pela palavra “Buzz”


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
