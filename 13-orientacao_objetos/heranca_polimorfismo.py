from time import sleep  # Importa a função sleep do módulo time
from random import randint  # Importa a função randint do módulo random

# Definição de valores fixos para os automóveis
VALOR_PEDAGIO_CARRO = 3.5
VALOR_PEDAGIO_MOTO = 2.75

VALOR_KM_RODADO_CARRO = 1.5
VALOR_KM_RODADO_MOTO = 1.0

# Classe base para Automóvel
class Automovel:
    numero_total_locacoes = 0
    def __init__(self, montadora, modelo, alugado):
        self.montadora = montadora
        self.modelo = modelo
        self.alugado = alugado
        self.valor_fatura = 0
        self.nome_cliente = ""
        print(f'Automóvel {self.montadora} {self.modelo} adquirido pela Locadora!')

    def alugar(self, nome_cliente):
        Automovel.numero_total_locacoes += 1
        self.alugado = True
        self.nome_cliente = nome_cliente
        print(f'O Automóvel {self.montadora} {self.modelo} foi alugado por {self.nome_cliente}!')

    def devolver_automovel(self):
        self.alugado = False
        print(f'O Automóvel {self.montadora} {self.modelo} foi devolvido por {self.nome_cliente}!')

    def gerar_valor_fatura(self, numero_pedagios, km_rodados, valor_pedagio):
        raise NotImplementedError  # A ser implementado nas subclasses

    @classmethod
    def mostrar_numero_total_locacoes(cls):
        print(f'O número total de Locações de Automóveis é de: {cls.numero_total_locacoes} locações')

# Subclasse Carro
class Carro(Automovel):
    numero_total_locacoes_carro = 0
    valor_total_locacoes = 0.0
    def __init__(self, montadora, modelo, alugado):
        super(Carro, self).__init__(montadora, modelo, alugado)
        print("O automóvel adquirido foi um Carro!")

    def alugar(self, nome_cliente):
        super(Carro, self).alugar(nome_cliente)
        Carro.numero_total_locacoes_carro +1
    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        # Cálculo da fatura para o Carro
        self.valor_fatura = numero_pedagios * VALOR_PEDAGIO_CARRO + km_rodados * VALOR_KM_RODADO_CARRO
        print(f'Fatura do Carro {self.montadora} {self.modelo} gerada com sucesso no valor R$ {self.valor_fatura:.2f}')
        Carro.valor_total_locacoes += self.valor_fatura

# Subclasse Moto
class Moto(Automovel):
    numero_total_locacoes_moto = 0
    valor_total_locacoes = 0.0

    def __init__(self, montadora, modelo, alugado):
        super(Moto, self).__init__(montadora, modelo, alugado)
        print("O automóvel adquirido foi uma Moto!")
    def alugar(self, nome_cliente):
        super(Moto, self).alugar(nome_cliente)
        Moto.numero_total_locacoes_moto +1

    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        # Cálculo da fatura para a Moto
        self.valor_fatura = numero_pedagios * VALOR_PEDAGIO_MOTO + km_rodados * VALOR_KM_RODADO_MOTO
        print(f'Fatura da Moto {self.montadora} {self.modelo} gerada com sucesso no valor R$ {self.valor_fatura:.2f}')
        Moto.valor_total_locacoes += self.valor_fatura

# Função para mostrar a fatura de um automóvel
def mostrar_fatura(automovel):
    print(f'O valor da Fatura do Automóvel {automovel.montadora} {automovel.modelo}'
          f' alugado por {automovel.nome_cliente} ficou no valor de R$ {automovel.valor_fatura:.2f}')

# ------------------------------------------------------------------------------------

# Criando uma instância de Carro (Ford Fiesta) e realizando operações
fiesta = Carro("Ford", "Fiesta", False)  # Instancia um carro
fiesta.alugar("João")  # Aluga o carro para João

# Simulando o tempo de aluguel do Automóvel
sleep(randint(7, 10))

fiesta.devolver_automovel()  # Devolve o carro

fiesta.gerar_valor_fatura(numero_pedagios=5, km_rodados=750)  # Calcula a fatura do carro
mostrar_fatura(fiesta)  # Mostra a fatura do carro

# Criando uma instância de Moto (Honda CB500) e realizando operações
honda_cb = Moto("Honda", "CB500", False)  # Instancia uma moto
honda_cb.alugar("Ana")  # Aluga a moto para Ana

# Simulando o tempo de aluguel do Automóvel
sleep(randint(7, 10))

honda_cb.devolver_automovel()  # Devolve a moto

honda_cb.gerar_valor_fatura(numero_pedagios=3, km_rodados=500)  # Calcula a fatura da moto
mostrar_fatura(honda_cb)  # Mostra a fatura da moto
