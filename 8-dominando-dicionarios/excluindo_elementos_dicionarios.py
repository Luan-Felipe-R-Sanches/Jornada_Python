fila = {
    '0': 'João',
    '1': 'Joana',
    '2': 'Clara',
    '3': 'Ana',
    '4': 'Julio',
}
print(f'Fila inicial: {fila}')

#del

del fila['0']
print(fila)

#pop

valor_retirado = fila.pop('1')
print(valor_retirado)
print(fila)

#popitem

valor_retirado = fila.popitem()
print(valor_retirado)
print(fila)

#clear

fila.clear()
print(fila)