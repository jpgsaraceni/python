"""
:s - str
:d - int
:f - float
:.<n>f - aproximar n casas
:<caractere> <sinal de <, > ou ^> <n> insere à direita, esquerda ou centro
    ]com n caracteres no total
"""
num = 10000
print(f'{num:a^3}')

print('{:@^50}'.format(num))

# índices
a = 'a'
b = 'b'
c = 'c'
print('{1}'.format(a, b, c))  # retorna a variável 1 do format (a partir do 0)

# colocando a variável e um ponto depois pode chamar diversas funções para formatar
print(a.upper())