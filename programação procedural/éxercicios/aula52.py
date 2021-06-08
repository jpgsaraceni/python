# 2


def mestre(funcao, *args, **kwargs):  # função vai receber uma função, não sabe quantos argumentos
    # ou argumentos nomeados.
    return funcao(*args, **kwargs)  # executa a função que receber com os argumentos que receber


def fala_oi(nome):
    return f'oi {nome}'


def saudacao(nome, oi):
    return f'{oi}, {nome}'


executando = mestre(fala_oi, 'Joao')
# passa a função fala_oi como argumento e
# Joao como um arg, que vai ser retornado como
# argumento da função fala_oi

executando2 = mestre(saudacao, 'Joao', 'oi')
# envia saudacao como argumento 1 de mestre, que a executa com os argumentos joao e oi para nome e saudacao.

print(executando)
print(executando2)
