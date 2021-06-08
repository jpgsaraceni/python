from varper import aumento, desconto
preco = 10
saida = aumento(valor=preco, percentual=10, formata=True)
print(f'O preço com juros é {saida}')
saida2 = desconto(valor=preco, percentual=10, formata=True)
print(f'O preço a vista é {saida2}')
