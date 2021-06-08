"""
listas, strings, etc. são objetos iteráveis
iter é o tipo de dado dos iteradores
iteradores retornam um valor de cada vez
geradores são usados para economizar memória. só salvam o valor que retornam naquele momento
a função next() retorna o próximo valor de um iterador
"""
ger = (x for x in range(100))  # gerador

# listas, tuples e string são sequences, sequences são iteráveis
# for converte sequencias em iteradores e usa a função next
# os valores utilizados dos iteradores e geradores são consumidos
