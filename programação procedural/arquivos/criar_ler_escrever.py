file = open('abc.txt', 'w+')  # abre arquivo
# 'w+' // zera o arquivo, leitura e escrita
file.write('Linha 1\n')  # escreve no arquivo
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0, 0)  # volta na linha x posição relativa y e lê o arquivo
print(file.read())  # lê o arquivo a partir daquele ponto

file.seek(0, 0)
print(file.readline())  # lê linha seguinte
print(file.readlines())  # lê as linhas em uma lista

file.close()  # fecha o arquivo
