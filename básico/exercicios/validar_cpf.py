while True:
    digitou = input('Insira o cpf (apenas números, 11 dígitos): ')  # receber o valor
    if digitou.isnumeric() and len(digitou) == 11:  # verificar se tem 11 números
        pass
    else:
        print('Valor inválido. Tente novamente. ')
        continue  # voltar ao início
    acumulador = 0
    reverso = 10  # valor que vai multiplicar cada dígito
    numero = digitou[:9]
    for indice in range(19):  # serão 19 valores multiplicados (10 a 2 depois 11 a 2)
        if indice > 8:  # quando chegar no último dígito volta ao primeiro
            indice -= 9
        acumulador += (int(numero[indice]) * reverso)
        reverso -= 1
        if reverso < 2:  # quando chegar ao último dígito
            v = 11 - (acumulador % 11)  # checar se o dígito cumpre a exigência
            if v > 9:
                d = 0
            else:
                d = v
            numero += str(d)    # adicionar o dígito ao cpf
            acumulador = 0  # zerar o acumulador para receber os valores agora dos 10 dígitos
            reverso = 11  # serão 10 dígitos agora
    sequencia = digitou[0]*11  # números repetidos burlam a regra
    if numero != digitou or digitou == sequencia:
        print('CPF inválido!')
    else:
        print('CPF válido!')
        cont = input('Deseja validar outro CPF? Digite s para sim ou n para não. ')
        if cont == 'n':
            break
