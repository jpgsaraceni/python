clientes = {
    'cliente1': {
            'nome': 'joao',
            'sobrenome': 'saraceni',
    },
    'cliente2': {
            'nome': 'zé',
            'sobrenome': 'batata',
    },
}

for clientes_k, clientes_v in clientes.items():  # iteração do dicionário mestre
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():  # acessar os dados de cada cliente
        print(f'\t{dados_k} = {dados_v}')

# esse código funciona para qualquer quantidade de clientes no dicionário mestre

# para copiar dic usar <var> = <dic>.copy() (cópia rasa)
# se usar apenas <var> = <dic>, os dois são o mesmo objeto na memória.

# .pop(<chave>) apaga ou .popitem() apaga último
# <dic>.update(<dic2>) para concatenar dicionarios
