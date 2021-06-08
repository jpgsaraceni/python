fatores_12 = list(range(5, 1, -1)) + list(range(9, 1, -1))
fatores_13 = list(range(6, 1, -1)) + list(range(9, 1, -1))

while True:
    cnpj_informado = input('Digite o CNPJ para validar (apenas números): ')
    if len(cnpj_informado) != 14 or not cnpj_informado.isdigit() or cnpj_informado == '00000000000000':
        print('Por favor, digite apenas números, com 14 casas. ')
    else:
        break

cnpj = cnpj_informado[:-2]


def digito(numero, fator):  # recebe sequencia e acrescenta um digito
    acumulador = 0
    contador = 0
    for i in numero:
        acumulador = int(i) * fator[contador] + acumulador
        contador += 1
    if (11 - (acumulador % 11)) > 9:
        numero += '0'
        return numero
    else:
        numero += str(11 - (acumulador % 11))
        return numero


verificado = digito(digito(cnpj, fatores_12), fatores_13)

if verificado == cnpj_informado:
    print('CNPJ válido!')
else:
    print('CNPJ inválido!')
