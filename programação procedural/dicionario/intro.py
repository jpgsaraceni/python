"""
dicionário - estrutura de dados que suporta um par de chaves e valor
similar a lista, porém vc cria o "índice".
"""
d1 = {'chave1': 'valor da chave'}  # cria dicionário
# d1['nova_chave'] = 'valor da nova chave'  # adiciona valor
# d1['chave1'] acessa uma chave

d2 = dict(chave1='valor da chave')  # outra maneira de criar

# chave deve ser única, se for definida mais de uma com o mesmo nome vale a última.
# qualquer valor imutável pode ser usada como chave

d3 = {
    'str': 'valor',
    123: 'int',
    (1, 2, 3, 4): 'tupla'  # p acessar, d3[(1, 2, 3, 4)]
}

# del d1['str']  # exclui a chave
# if 'str' in d1  # checa se há essa chave no dic
# 'valor' in d1.values() checa se há o valor
# len retorna quantos pares há

# dicionários são iteráveis (pode usar for)
# d1.items() acessa os pares como tuples


