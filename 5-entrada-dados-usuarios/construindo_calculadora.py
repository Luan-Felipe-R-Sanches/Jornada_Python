numero_1 = input('Digite o primeiro numero: ')
numero_2 = input('Digite o segundo numero: ')
print('Digite a operação:\n\t+ para Adição\n\t- para Subtração\n\t* para Multiplicação\n\t/ para Divisão')

operacao = input('Digite a operação: ')

equacao = f'{numero_1} {operacao} {numero_2}'

resultado = eval(equacao)

print(f'{"*" * 25}\nResultado: {resultado}\n{"*" * 25}')