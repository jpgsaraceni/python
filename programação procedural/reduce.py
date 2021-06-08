# acumulador
from dados import lista
from functools import reduce
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
