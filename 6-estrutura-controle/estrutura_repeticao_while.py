from random import  randint

CAPACIDADE_MAXIMA_BALDE = 1000

balde = 0

while balde <= CAPACIDADE_MAXIMA_BALDE:
    volume_copo = randint(95, 100)
    print(f'O copo foi enchido com {volume_copo}mls')

    balde += volume_copo
    print(f'O volume do balde é de {balde}mls\n')
print(f'O volume do balde ultrapassou a capacidade máxima de {CAPACIDADE_MAXIMA_BALDE}mls e está com {balde}mls')