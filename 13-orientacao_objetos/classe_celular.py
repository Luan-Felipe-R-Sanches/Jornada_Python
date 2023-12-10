# Classe Celualar:
#  Atributos:
#   Fabricante: String
#   Modelo: String
#   Tela: Decimal
#   Armazenamento: Inteiro
#   Memória: Inteiro
#   Câmera: Inteiro
#   Bateria: Inteiro
#   Tela ligada: Booleano
# Métodos:
#   ligar_tela()
#   salvar_em_disco()
#   carregar_aplicativo()
#   tirar_foto()
#   verificar_carga_bateria()
from random import random


class Celular:
    def __init__(self, fabricante, modelo, tela, armazenamento, memoria, camera, bateria, tela_ligada):
        self.fabricante = fabricante
        self.modelo = modelo
        self.tela = tela
        self.armazenamento = armazenamento
        self.memoria = memoria
        self.camera = camera
        self.bateria = bateria
        self.tela_ligada = tela_ligada

    def verificar_carga_bateria(self):
        # random() retorna um float de [0, 1)

     porcentagem_bateria = random()
     carga_atual = self.bateria * porcentagem_bateria
     bateria_restante = self.bateria - carga_atual
     print(f'O celular está com {porcentagem_bateria:.0f}% de bateria e {bateria_restante:.0f}mA restantes')

    def ligar_tela(self):
        self.tela_ligada = True

celular_android = Celular("Samsung", "S10", 6.25, 128, 4, 21,
                          3400, False)
celular_iphone = Celular(fabricante="Apple", modelo="Iphone 13 PRO", tela=5.75, armazenamento=128, memoria=3, camera=16,
                         bateria=2650, tela_ligada=False)

celular_iphone.ligar_tela()
print(celular_iphone.tela_ligada)