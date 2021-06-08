def lista_clientes(clientes, lista=()):
    lista = list(lista)  # usei a tupla por ser imutável
    lista.extend(clientes)
    return lista


clientes1 = ['João', 'Maria', 'Eduardo']
clientes2 = ['Marcos', 'Jonas', 'Zico']
clientes3 = ['José']

print(clientes1)
print(clientes2)
