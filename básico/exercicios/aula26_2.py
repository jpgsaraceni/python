h = input('digite a hora ')
m = input('digite o minuto ')

if h.isdigit() and m.isdigit():
    h = int(h)
    m = int(m)
    if h > 23 or h < 0 or m < 0 or m > 59:
        print('digite hora entre 0 e 23 e minuto entre 0 e 59')
    else:
        if h < 12:
            print('bom dia')
        else:
            if h == 12:
                if m == 0:
                    print('bom dia')
                else:
                    print('boa tarde')
            else:
                if h < 18:
                    print('boa tarde')
                else:
                    print('boa noite')
else:
    print('valor inválido')
