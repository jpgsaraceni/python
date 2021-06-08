"""
para comentários vide validar_cpf.py
"""
while True:
    from random import randint  # módulo do python
    numero = str(randint(100000000, 999999999))  # número de 9 dígitos aleatório
    acumulador = 0
    reverso = 10
    for indice in range(19):
        if indice > 8:
            indice -= 9
        acumulador += (int(numero[indice]) * reverso)
        reverso -= 1
        if reverso < 2:
            reverso = 11
            v = 11 - (acumulador % 11)
            if v > 9:
                d = 0
            else:
                d = v
            numero += str(d)
            acumulador = 0
    print(numero)
    cont = input('Deseja gerar outro CPF? Digite s para sim ou n para não. ')
    if cont == 'n':
        break
