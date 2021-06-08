from dados import produtos, pessoas, lista

nova_lista = map(lambda x: x * 2, lista)  # retorna iterador map
print(lista)
print(list(nova_lista))

nova_lista2 = [x for x in lista]    # mesmo resultado
print(nova_lista2)

precos = map(lambda p: p['preco'], produtos)  # acessa a chave preco em cada dict


def aumento(dic):   # função para aplicar aumento
    dic['preco'] = round(dic['preco'] * 1.05, 2)    # arredonda 2 casas
    return dic


novos_produtos = map(aumento, produtos)  # criar novo dict
for produto in novos_produtos:
    print(produto)

# map passa uma função em cada elemento de um iterável

nomes = map(lambda n: n['nome'], pessoas)
for pessoa in nomes:
    print(pessoa)
