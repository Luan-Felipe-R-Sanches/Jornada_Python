cadastro ={
    'id':1,
    'nome': 'João Carlos Silva',
    'filhos': ['Joana', 'Sarah'],
    'compras':[
        {
            'id': 4758,
            'produto': 'Notebook Gamer',
            'preco': 2597.99
        }
    ]
}
print(f"O usuário {cadastro['nome']} realizou a seguinte compra: {cadastro['compras'][0]['produto']}")

filhos = cadastro.get('filhos')
print(filhos)