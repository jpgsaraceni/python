while True:
    n1 = input('Digite um número: ')
    if not n1.isnumeric():
        print('Isso não é um número. Tente novamente.')
        continue
    n2 = input('Digite outro número: ')
    if not n2.isnumeric():
        print('Isso não é um número. Tente novamente.')
        continue
    op = input('Digite o operador: ')
    if not ((op == '+') or (op == '-') or (op == '*') or (op == '/')):
        print('Operador inválido. Tente novamente.')
        continue
    else:
        n1 = int(n1)
        n2 = int(n2)
        if op == '+':
            print(n1 + n2)
        elif op == '-':
            print(n1 - n2)
        elif op == '*':
            print(n1 * n2)
        else:
            print(n1 / n2)
    sair = input('Digite 1 se deseja sair ou 2 se deseja fazer outra operação. ')
    if sair == '1':
        break
    else:
        continue
