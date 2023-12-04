def monta_computador(cpu, memoria, hd, *precos, monitor=17, **outros_atributos):
    print('O computador montado foi: ')
    print(f'\tCPU: {cpu}')
    print(f'\tMemória: {memoria}Gb')
    print(f'\tHD: {hd}tb')
    print(f'\tPreços praticados: {precos}')  # Imprime os preços fornecidos

    for preco in precos:
        print(f'\t\t{preco}')  # Imprime cada preço individualmente

    print(f'\tMonitor: {monitor} polegadas')  # Imprime o tamanho do monitor
    print('\tOutros Atributos: ')

    for chave, valor in outros_atributos.items():  # Imprime outros atributos
        print(f'\t\t{chave}: {valor}')

monta_computador('Core i7', 16, 2, 2500, 3199, 4200, monitor=25, webcam='Webcam Multilaser', teclado='Teclado Multilaser')
print(teste)