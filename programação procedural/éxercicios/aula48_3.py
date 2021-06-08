def conta(valor, perc):
    return valor * (1 + perc / 100)


a = float(input('Digite um valor: '))
b = float(input('Digite um percentual: '))
print(conta(a, b))
