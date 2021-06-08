from formata.moeda import converter


def aumento(valor, percentual, formata=False):
    r = valor + (valor * percentual / 100)

    if formata:
        return converter(r)
    else:
        return r


def desconto(valor, percentual, formata=False):
    r = valor - (valor * percentual / 100)

    if formata:
        return converter(r)
    else:
        return r
