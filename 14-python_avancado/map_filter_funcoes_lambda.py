cadastros = [
    "João,18,joao@e'mail.com",
    "   Jo'ana,22,joana@gmail.com    ",
    "Kléber,30,kleber123@hotmai'l.com"
]

# Usando map para substituir as aspas simples por nada e remover espaços extras
resultado = list(map(lambda texto: texto.replace("'", "").strip(), cadastros))

print(resultado)

# Filtrando apenas os e-mails que contenham '@gmail'
resultado_filter = list(filter(lambda cadastro: '@gmail' in cadastro, resultado))

print(resultado_filter)
