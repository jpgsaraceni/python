"""
similar a lista, porém só aceita valores únicos
<set> = {a, b, c, ...}
não tem índice, não acessa valor diretamente mas pode iterar
set vazio - set()
adicionar valores ao set - <set>.add(<valor>)
remover - .discard(<valor>)
.update itera sobre o elemento a ser acrescentado
set não tem ordem para os elementos.
pode fazer casting de e para set.
"""
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3, 4, 5, 6}
s3 = s1.union(s2)  # ou s1 | s2
s4 = s1 & s2  # interseção
s5 = s1 - s2  # diferença
s6 = s1 ^ s2  # AUB - A int B
