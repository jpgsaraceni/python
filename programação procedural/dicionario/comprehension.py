lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
]

d1 = {x.upper(): y*2 for x, y in lista}
print(d1)
