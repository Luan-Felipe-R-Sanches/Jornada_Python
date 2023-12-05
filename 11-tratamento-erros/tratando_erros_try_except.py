def divide_dois_numeros(dividendo, divisor):
    return  dividendo/divisor

try:
    # Código a ser testado
    numero_1 = int(input("Digite o primeiro número: "))
    numero_2 = int(input("Digite o segundo número: "))

    resultado = divide_dois_numeros(numero_1, numero_2)
    print(resultado)

except (ZeroDivisionError, TypeError) as excecao:
    print(f"Divisão por zero não suportada ou Erro de Tipagem. Erro:{excecao} ")

finally:
    # Sempre execute esse codigo
    print("Finalizando programa... Muito obrigado!")