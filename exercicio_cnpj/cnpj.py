from random import randint
fatores_12 = list(range(5, 1, -1)) + list(range(9, 1, -1))
fatores_13 = list(range(6, 1, -1)) + list(range(9, 1, -1))


def gerar():
    numero = str('{:0>12}'.format(randint(1, 999999999999)))
    cnpj_gerado = calcular_digitos(calcular_digitos(numero, fatores_12), fatores_13)
    return formatar_cnpj(cnpj_gerado)


def calcular_digitos(numero, fator):
    if not (numero.isdigit() or len(numero) == 14 or numero == '00000000000000'):
        return '0'
    total = 0
    for i, fator in enumerate(fator):  # evita criar acumulador e contador
        total += int(numero[i]) * total
    if (11 - (total % 11)) > 9:
        numero += '0'
        return numero
    else:
        numero += str(11 - (total % 11))
        return numero


def formatar(cnpj_informado):
    cnpj_informado.replace('/', '')
    cnpj_informado.replace('.', '')
    cnpj_informado.replace('-', '')
    cnpj_formatado = cnpj_informado
    return cnpj_formatado


def reduzir(formatado):
    cnpj_reduzido = formatado[:-2]
    return cnpj_reduzido


def verificar(num1, num2, msg_ok, msg_not):
    if num1 == num2:
        print(msg_ok)
        return True
    else:
        print(msg_not)
        return False


def formatar_cnpj(cnpj):
    formatado = cnpj[0:2] + '.' + cnpj[2:5] + '.' + cnpj[5:8] + '/' + cnpj[8:12] + '-' + cnpj[12:]
    return formatado


def validar_cnpj(cnpj):
    if (not formatar(cnpj).isdigit()) or len(formatar(cnpj)) != 14 or formatar(cnpj) == '00000000000000':
        print('Formato inválido. Verifique o CNPJ e tente novamente.')
    else:
        verificado = calcular_digitos(calcular_digitos(reduzir(formatar(cnpj)), fatores_12), fatores_13)
        verificar(verificado, cnpj, f'CNPJ {formatar_cnpj(verificado)} válido.', 'CNPJ inválido.')
