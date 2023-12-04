def soma(maximo, *numeros):
    resultado = 0  # Inicializa o resultado da soma como zero
    numeros_somados = []  # Lista para armazenar os números que foram somados

    for numero in numeros:  # Itera sobre os números fornecidos
        if (resultado + numero) > maximo:  # Verifica se a adição excede o limite máximo
            break  # Se a soma ultrapassar o máximo, encerra o loop
        resultado += numero  # Adiciona o número ao resultado da soma
        numeros_somados.append(numero)  # Adiciona o número à lista de números somados

    return resultado, numeros_somados  # Retorna o resultado da soma e a lista de números somados

# Chama a função 'soma' com limite máximo 100 e os números 2, 5 e 10
resultado_somado, numeros_somados = soma(100, 2, 5, 10)

# Imprime o resultado da soma
print(resultado_somado)

# Imprime os números que foram somados até atingir o limite máximo
print(numeros_somados)
