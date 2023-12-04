# Faça um programa que verifique se uma pessoa tem idade suficiente para
# votar (idade igual ou superior a 18 anos).

idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você pode votar!")
else:
    print("Não pode votar!")