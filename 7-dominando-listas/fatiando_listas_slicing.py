#          0    1    2    3    4    5
letras = ['a', 'b', 'c', 'd', 'e', 'f']
#         -6   -5   -4   -3   -2    -1

print(letras[0:3:1])
print(letras[3:6:1])
print(letras[::-1])
print(letras[-6:-3:1])
print(letras[-3::1])
print(letras[::2] + letras[1::2])