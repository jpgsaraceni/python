lista_1 = [1, 2, 3, 4, 5, 6, 7]
lista_2 = [1, 2, 3, 4]
# lista_3 = [x + y for x, y in zip(lista_1, lista_2)]

lista_3 = zip(lista_1, lista_2)

for valor in lista_3:
    print(valor[1]+valor[0])
