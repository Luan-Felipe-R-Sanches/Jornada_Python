# Função que realiza a soma de dois números
def soma(numeros):
    return int(numeros[0]) + int(numeros[1])

# Função que realiza a divisão do primeiro número pelo segundo
def divisao(numeros):
    return int(numeros[0]) / int(numeros[1])

# Função que realiza a subtração do segundo número do primeiro
def subtracao(numeros):
    return int(numeros[0]) - int(numeros[1])

# Função que realiza a multiplicação de dois números
def multiplicacao(numeros):
    return int(numeros[0]) * int(numeros[1])

# Solicita dois números separados por espaço e os armazena em uma lista
numeros_input = input('Digite os números separados por espaço: ').split(' ')

# Solicita a operação desejada (+, -, *, /) ao usuário
operacao_input = input('Digite a operação (+ / - *): ')
resultado_calculo = 0

# Verifica se a quantidade de números fornecidos é diferente de 2
if len(numeros_input) != 2:
    print('Quantidade de entradas diferente de 2')
else:
    # Verifica se a operação inserida está entre as operações suportadas (+, -, *, /)
    if operacao_input in '+/-*':
        # Executa a operação correspondente aos números fornecidos
        if operacao_input == '+':
            resultado_calculo = soma(numeros_input)
        elif operacao_input == '/':
            resultado_calculo = divisao(numeros_input)
        elif operacao_input == '-':
            resultado_calculo = subtracao(numeros_input)
        elif operacao_input == '*':
            retultado_calculadora = multiplicacao(numeros_input) # Há um erro de digitação aqui (retultado_calculadora -> resultado_calculo)

        # Exibe o resultado da operação na tela
        print(f'Resultado: {resultado_calculo}') # Há um erro de digitação aqui (retultado_calculadora -> resultado_calculo)
    else:
        # Informa que a operação inserida é inválida
        print(f'Operação {operacao_input} inválida')
