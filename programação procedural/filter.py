from dados import pessoas, lista, produtos

nova = filter(lambda x: x > 5, lista)  # retorna v ou f para cada elemento
nova2 = [x for x in lista if x > 5]
print(list(nova))
print(list(nova2))

nova3 = filter(lambda p: p['preco'] > 10, produtos)
