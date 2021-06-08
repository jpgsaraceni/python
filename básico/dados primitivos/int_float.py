"""
int - inteiro
float - real/ponto flutuante
"""
print(type(2))  # type retorna o tipo de dado
print(type(2.0))
print(2 > 3)  # operador booleano, retorna True ou False
# escrever o tipo de dado antes converte no que está escrito (casting)
print(type(float(2)))

'''
operadores matemáticos:
+, -, *, /
// divisão inteira (arredondado)
** exponenciação
% módulo (resto da divisão)
() 
'''

# .isdigit() checa se o valor pode ser transformado em int

# :.<n>f retorna o número de casas decimais arredondado
num = 1.1268
print(f'{num:.2f}')
# ou
print('{:.2f}'.format(num))

# formatar como inteiro :d e formatar como float :f
