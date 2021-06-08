"""
São funções anônimas, com pouco código
usado para passar uma função como argumento.
sintaxe é lambda <argumentos>: <retorno>
"""
lista = [
    ['P1', 12],
    ['P2', 13],
    ['P3', 5],
    ['P4', 32],
]


def func(item):
    return item[1]  # acessar o y de cada vetor


lista.sort(key=func, reverse=True)  # ordena segundo a função em ordem dec
print(lista)

# pode usar sorted() sem alterar a lista

print(sorted(lista, key=lambda i: i[1]))  # função anonima
#                             arg  ret

