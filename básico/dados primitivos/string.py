# str ou string é um texto dentro de aspas, simples ou duplas.
"""
por ser uma linguagem de tipagem dinâmica, o python
entende que o que está dentro de aspas é uma string.
"""
# barra invertida é caractere de escape
# faz o programa ignorar o próximo caractere.
print('Hello \'mandafaca\'')
# \n quebra a linha.
# r dentro da string faz com que não execute comandos
print(r'blabla \n bla')  # não quebra
print('blabla \nbla')  # quebra

print(f'assim pode inserir variável na string usando chaves')
num = 3.1234
print(f'assim {num:.1f}')  # número de casas decimais

print('pode colocar chave vazia na string e depois .format(variáveis)')
# pode colocar .<n>f para casas decimais
# dentro da chave pode colocar um número para a posição da variável no .format
# ou nomear os parametros dentro das chaves

# função len retorna número de caracteres (int)
# len(<variável>)

# formatar como string :s

# cada caractere de uma string é um índice, a partir do 0.
# para acessar um caractere: <variável>[n] sendo n o indice
text = '12345'
print(text[4])
# usando um - na frente conta a partir do último caractere (1)
print(text[-1])
# para fatiar uma string usar [<inicio>:<fim>], excluindo o fim.
# Se for do início, apenas [:<fim>]. até o fim análogo.
print(text[1:4])
# índice [<n>:<m>:<p>] p é o passo de quais imprimir
print(text[:5:2])

# .strip remove espaço no início e fim da string

# .replace troca o caractere
