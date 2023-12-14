# Importa a biblioteca necessária
from __future__ import annotations
from dataclasses import dataclass

# Cria uma classe simples usando dataclass
@dataclass
class Ponto:
    x: int
    y: int

# Função que faz a correspondência de padrões
def identificar_ponto(ponto: Ponto) -> str:
    match ponto:
        case Ponto(0, 0):
            return "Origem"
        case Ponto(0, y):
            return f"Eixo Y no valor {y}"
        case Ponto(x, 0):
            return f"Eixo X no valor {x}"
        case Ponto(x, y):
            return f"Ponto em ({x}, {y})"

# Cria alguns pontos
ponto1 = Ponto(0, 0)
ponto2 = Ponto(0, 5)
ponto3 = Ponto(10, 0)
ponto4 = Ponto(3, 7)

# Testa a função com diferentes pontos
print(identificar_ponto(ponto1))  # Saída: Origem
print(identificar_ponto(ponto2))  # Saída: Eixo Y no valor 5
print(identificar_ponto(ponto3))  # Saída: Eixo X no valor 10
print(identificar_ponto(ponto4))  # Saída: Ponto em (3, 7)
