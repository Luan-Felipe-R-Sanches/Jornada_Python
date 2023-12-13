class NumerosPares:
    def __init__(self, maximo):
        self.maximo = maximo  # Define o valor máximo para os números pares
        self.atual = 0  # Inicializa o número atual como 0

    def __iter__(self):
        return self  # Retorna a própria instância da classe como um iterador

    def __next__(self):
        if self.atual > self.maximo:  # Verifica se o número atual ultrapassou o máximo
            raise StopIteration  # Levanta a exceção StopIteration para indicar o fim da iteração

        retorno = self.atual  # Armazena o número atual para ser retornado

        self.atual += 2  # Incrementa o número atual em 2 para obter o próximo número par

        return retorno  # Retorna o número atual para a iteração

# Cria uma instância de NumerosPares com um limite de 150
iterador_numeros_pares = NumerosPares(maximo=150)

# Itera sobre os números pares usando o iterador personalizado
for numero in iterador_numeros_pares:
    print(numero, end=" ")

# Função geradora para números pares
def numeros_pares(maximo):
    atual = 0  # Inicializa o número atual como 0

    while atual < maximo:  # Enquanto o número atual for menor que o máximo fornecido
        yield atual  # Retorna o número atual usando yield

        atual += 2  # Incrementa o número atual em 2 para obter o próximo número par
