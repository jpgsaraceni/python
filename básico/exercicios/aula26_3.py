nome = input('Digite seu primeiro nome')
# poderia criar variável tamanho e usar abaixo
if len(nome) <= 4:
    print('Seu nome é curto')
else:
    if len(nome) == 5 or len(nome) == 6:
        print('seu nome é normal')
    else:
        print('seu nome é grande')
