# Definição da classe Pessoa
class Pessoa:
    def __init__(self, nome, idade, cidade, genero):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.genero = genero

# Lista de objetos Pessoa
pessoas = [
    Pessoa('João', 20, 'Belém', 'M'),
    Pessoa('Catarina', 31, 'Brasília', 'F'),
    Pessoa('Ana', 38, 'Brasília', 'F'),
    Pessoa('Joana', 28, 'Natal', 'F'),
    Pessoa('Henrique', 35, 'Palmas', 'M'),
    Pessoa('Alberto', 15, 'Goiania', 'M')
]

# Conjunto de cidades únicas a partir dos objetos Pessoa
cidade = {pessoa.cidade for pessoa in pessoas}
print(cidade)

# Conjunto de nomes iniciados com 'J' a partir dos objetos Pessoa
pessoas_iniciadas_com_j = {pessoa.nome for pessoa in pessoas if pessoa.nome[0] == 'J'}
print(pessoas_iniciadas_com_j)
