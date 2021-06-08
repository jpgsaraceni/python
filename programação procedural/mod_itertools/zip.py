# função zip une iteráveis formando tuplas como iterável
# retorna um zip object, pode fazer casting para ser uma lista de tuplas e.g.

# a função zip_longest está no módulo itertools
from itertools import zip_longest, count
# se um iterável não tiver a mesma quantidade de valores da outra, preenche com None
# usar fillvalue=<valor> para substituir o none

# exemplo aula
indice = count()  # pode usar start=n e step=n dentro do parenteses.
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(
    indice,
    estados,
    cidades
)
for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)
