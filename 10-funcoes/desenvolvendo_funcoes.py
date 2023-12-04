def calcula_media_mediana(notas):
    # Calcula a média das notas
    media = sum(notas) / len(notas)

    if len(notas) % 2 == 0:
        # Se o número de elementos é par, calcula a mediana
        indice_ponto_central_menor = int(len(notas)/2 - 1)
        indice_ponto_central_maior = int(len(notas)/2)
        ponto_central_menor = notas[indice_ponto_central_menor]
        ponto_central_maior = notas[indice_ponto_central_maior]

        # Calcula a mediana para números pares
        media = (ponto_central_menor + ponto_central_maior) / 2
    else:
        # Se o número de elementos é ímpar, calcula a mediana ordenando as notas
        notas_ordenadas = sorted(notas)
        indice_mediana = int(len(notas) / 2)
        mediana = notas_ordenadas[indice_mediana]

    # Retorna a média e a mediana (se calculada)
    return media, mediana

# Chama a função e passa a lista de notas
resultado_media, resultado_mediana = calcula_media_mediana([5, 6, 4])

# Imprime os resultados
print(resultado_media)   # Imprime a média
print(resultado_mediana) # Imprime a mediana
