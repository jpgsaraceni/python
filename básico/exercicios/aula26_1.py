num = input('digite um número inteiro ')
if num.isdigit():  # ou if not num.isdigit() ...
    num = int(num)
    if num % 2 == 0:
        print('o número é par')  # ou f'{num} é par
    else:
        print('o número é ímpar')  # análogo
else:
    print('número inválido.')
