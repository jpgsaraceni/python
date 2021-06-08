perguntas = {
    'Pergunta 1': {
        'pergunta': 'Qual é a capital do Canadá?',
        'respostas': {
            'A': 'Toronto',
            'B': 'Ottawa',
            'C': 'Montreal',
            'D': 'Vancouver',
        },
        'resposta_certa': 'B'
    },  # copiar até essa linha para criar perguntas.
    'Pergunta 2': {
        'pergunta': 'Qual é a capital de Portugal?',
        'respostas': {
            'A': 'Lisboa',
            'B': 'Porto',
            'C': 'Braga',
            'D': 'Benfica',
        },
        'resposta_certa': 'A'
    },
}

contador = 0
contadorp = 0

for pk, pv in perguntas.items():
    contadorp += 1
    print(f'{pk}: {pv["pergunta"]}')

    for rk, rv in pv['respostas'].items():
        print(f'[{rk}] {rv}')
    resposta_u = input('Digite a opção correta: ')
    if resposta_u == pv['resposta_certa']:
        print('Boa, espertão.')
        contador += 1
    else:
        print('Deixa de ser burro!')
    print()

print(f'Você acertou {contador} de {contadorp}')
