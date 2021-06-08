carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

# exercício é somar os valores em uma linha de codigo
total = sum([v for p, v in carrinho])
print(total)
