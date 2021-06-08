secreta = 'abacaxi'
palavra = []
chances = 3
while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Uma letra só, viado!')
        continue

    if letra in secreta:
        print(f'Beleza, tem {letra} na palavra.')
        palavra.append(letra)

    else:
        print(f'Tem {letra} não.')
        chances -= 1

    temp = ''                           # cria uma string vazia
    for letra_temp in secreta:          # percorre cada letra da palavra secreta
        if letra_temp in palavra:       # se a letra tiver sido digitada, coloca aqui
            temp += letra_temp
        else:
            temp += '_'
    print(temp)

    if temp == secreta:
        print('PARABENS VOCÊ VENCEU NADA!')
        break

    if chances > 1:
        print(f'Você ainda tem {chances} chances')
    if chances == 1:
        print(f'Você só tem {chances} chance')
    if chances == 0:
        print('SE FODEU')
        break
    print('')
