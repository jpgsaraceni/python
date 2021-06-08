"""
Lista é um tipo de dado (é um vetor).
Pode ter como elementos qualquer tipo de dados (pode misturar)
Cada elemento está associado a um índice, análogo às str
mesmas regras de fatiamento e range das str
"""
exemplo = ['índice 0', 'índice 1', 'etc.', 'a']
# pode acessar o índice e alterar para qualquer tipo de dado diretamente
# exemplo[1] = 4

# + entre duas listas (mesmo numéricas) é concatenar
# .extend(<lista>) concatena na lista. pode só um termo também.
# .append(<valor>) insere o valor ao final da lista
# .insert(<n>, <v>) insere v no índice n
# .pop() tira o último elemento
# del(<lista>[<range>]) apaga valores
# max(<lista>) e min(<lista>)
# list(range(n,m)) retorna uma lista de n a m-1.

i = 0
for x in exemplo:
    print(exemplo[i])
    i += 1

# .startswith(<caractere>)
# .lower()

# aceita lista dentro de lista (como matriz)

"""
lista = [1, 2, 3, 4]
a, b, c, d = lista  # atribui cada elemento a cada var - desempacotamento
se colocar asterisco antes de uma var cria uma lista com os elementos que sobram.
a, *lista2, d = lista # lista2 recebe 2 e 3.
por convenção usar *_ para não usar os outros elementos da lista.
"""
lista = [1,2,3,4]
a, b, *n = lista  # *n pega o resto da lista
print(a, b)
print(*lista)  # desempacota
