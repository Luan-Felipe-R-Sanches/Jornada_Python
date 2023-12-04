def aplica_bashara(a: float, b: float, c: float) -> (float, float):
    delta = b** 2 - 4 * a * c
    x_1 = (-b + (delta ** 1/2)) / (2 * a)
    x_2 = (-b - (delta ** 1/2)) / (2 * a)

    return  x_1, x_2

print(aplica_bashara(5, 15, -25))