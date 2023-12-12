# Dicionário com informações de salário de funcionários
cadastro = {
    'Maria': 4500,
    'Marcos': 7800,
    'Gabriel': 3750,
    'João': 15000
}

# Cria um novo dicionário contendo apenas os funcionários cujos salários são maiores que 5000
salario_maior_5000 = {chave: valor for chave, valor in cadastro.items() if valor > 5000}

# Imprime o novo dicionário contendo apenas os funcionários com salário maior que 5000
print(salario_maior_5000)
