computador = {
    'cpu': 'Core i7',
    'ram': 'DDR 16GB',
    'ssd': 'Samsung Evo 840 256GB',
    'gpu': 'RTX 2080 Ti'
}
print(f'Computador v1: {computador}' )

computador['ram'] = 'DDR4 32Gb'

print(f'Computador v2: {computador}')

computador['fonte'] = 'Fonte 600w Cosair'

print(f'Computador v3: {computador}')

computador.update({'fonte': 'Fonte 850W Corsair', 'ssd': 'Samsung Evo 840 1TB'})

print(f'Computador v4: {computador}')