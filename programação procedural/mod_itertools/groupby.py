from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rose', 'nota': 'C'},
    {'nome': 'João', 'nota': 'D'},
    {'nome': 'Joana', 'nota': 'A'},
    {'nome': 'Luiza', 'nota': 'B'},
    {'nome': 'Lu', 'nota': 'A'},
    {'nome': 'Lia', 'nota': 'C'},
    {'nome': 'Ana', 'nota': 'B'},
]


def ordena(item):   # ou: ordena = lambda item: item['nota']
    return item['nota']


alunos.sort(key=ordena)  # ordenando a lista segundo a chave 'nota'
alunos_agrupados = groupby(alunos, ordena)  # agrupar
# groupby(<var>, <chave>), agrupa segundo a chave

for agrupamento, valores_agrupados in alunos_agrupados:  # acessar o que usou para ordenar e os valores no groupby
    va1, va2 = tee(valores_agrupados)  # criar uma cópia do iterador usado

    print(f'Agrupamento: {agrupamento}')  # o que usou para agrupar

    for aluno in va1:  # cópia do que usou para agrupar (pois iterador original foi esgotado)
        print(f'\t{aluno}')

    quantidade = len(list(va2))  # número de alunos em cada grupo do groupby
    if quantidade == 1:
        a = 'aluno tirou'
    else:
        a = 'alunos tiraram'
    print(f'\t{quantidade} {a} a nota {agrupamento}')
    print()
# para usar groupby os valores precisam estar ordenados.
