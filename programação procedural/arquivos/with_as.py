with open('def.txt', 'w+') as file:  # cria e fecha sozinho ao final
    file.write('Linha1\n')
    file.write('Linha2\n')

    file.seek(0)
    print(file.read())

# usar 'r' no lugar do 'w+' apenas leitura
# 'a' coloca o cursor no final do arquivo (não apaga como w)
# + para ler e escrever

# apagar arquivo:
import os
os.remove('abc.txt')
