# 1) Ler aquivo de entrada CSV
# 2) Processamento (Retirada do campo ID e junção do campo NOME e SOBRENOME)
# 3) Gravação do arquivo de CSV de sáida

resultado = []
with open("./dados/cadastro.csv", "r") as arquivo_entrada:
    linhas = arquivo_entrada.readlines()[1:]  # Ignora o cabeçalho, começando da segunda linha

    for linha in linhas:
        dados = linha.strip().split(',')
        email = dados[3]
        nome_completo = f'{dados[1]} {dados[2]}'
        resultado.append(f'{nome_completo},{email}\n')  # Adiciona '\n' para quebras de linha

with open("./dados/cadastro_saida.csv", "w") as arquivo_saida:
    for linha in resultado:
        arquivo_saida.write(linha)
