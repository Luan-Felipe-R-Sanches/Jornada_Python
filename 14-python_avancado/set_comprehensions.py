# Definição da classe Pessoa
class Pessoa:
    def __init__(self, nome, idade, cidade, genero):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.genero = genero

# Lista de objetos Pessoa
pessoas = [
    Pessoa("João", 20, "Belém", "M"),
    Pessoa("Catarina", 31, "Brasília", "F"),
    Pessoa("Ana", 38, "Brasília", "F"),
    Pessoa("Joana", 28, "Natal", "F"),
    Pessoa("Henrique", 35, "Palmas", "M"),
    Pessoa("Alberto", 15, "Goiânia", "M")
]

# Conjunto de cidades únicas a partir dos objetos Pessoa
cidades = {pessoa.cidade for pessoa in pessoas}

# Conjunto de pessoas cujos nomes começam com 'J'
pessoas_iniciadas_com_j = {pessoa for pessoa in pessoas if pessoa.nome[0] == "J"}

# Conjunto de pessoas com idade superior a 30 anos
pessoas_maiores_30 = {pessoa for pessoa in pessoas if pessoa.idade > 30}

# Conjunto de pessoas do sexo masculino
pessoas_sexo_masculino = {pessoa for pessoa in pessoas if pessoa.genero.upper() == "M"}

# Impressão das informações obtidas nos conjuntos
# Imprime as cidades únicas
for cidade in cidades:
    print(cidade)

# Imprime os nomes das pessoas cujos nomes começam com 'J'
for pessoa in pessoas_iniciadas_com_j:
    print(f"Nome: {pessoa.nome}")

# Imprime os nomes e idades das pessoas com mais de 30 anos
for pessoa in pessoas_maiores_30:
    print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}")

# Imprime os nomes e gêneros das pessoas do sexo masculino
for pessoa in pessoas_sexo_masculino:
    print(f"Nome: {pessoa.nome}, Gênero: {pessoa.genero}")
