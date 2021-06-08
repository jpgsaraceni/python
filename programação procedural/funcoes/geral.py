"""
para definir uma nova função:
def <função>():
pode definir um argumento entre parênteses (uma ou mais variáveis)
"""


def saudar(msg='Olá', nome='mundo'):  # opcional definir padrão
    print(f'{msg}, {nome}!')  # dentro da hierarquia pode colocar quantas linhas quiser
# retorna sempre um valor. Se não definir, retorna None (não valor).
# return <valor>. função termina no return.
# uma função pode retornar outra função sem executar.

# >>>>> se definir parametro nos parenteses, tem que enviar quando chamar a função


saudar('Oi', 'amigo')  # posso colocar o nome da variável ou não
saudar()  # usa padrão
saudar(nome='banana')  # pode definir só uma var e outra padrão

# >>>>>>>>> variável pode receber valor do return <var> = <funcao>()
# >>>>>>>>> pode fazer isso com os valores dos argumentos entre parenteses

# >>>>>>>>> se usar só a função sem o parenteses, ela não é executada!!!!!

# Quando colocar um valor padrão para um argumento, os que seguem devem receber tbm.
# se o valor padrão for None, não precisa usar esse argumento.

# se não souber quantos argumentos virão, usar *args. vem empacotados em tupla


def f(*args):  # *args é por convenção.
    print(args)


f(1,2,3)  # tupla

# tupla não pode alterar valor. pode fazer cast para lista.

# **kwargs são argumentos nomeados.
# para acessar o kwarg, usar kwarg['<key>']. se não tiver certeza que será definido, usar get.
# <key> = kwargs.get('<key>')

# quando editar a variável de uma função, torna-se local (não global)
# pode usar global <variavel> dentro da função para alterar global, mas evitar.
# não pode usar como global depois local.

# >>>> assinatura da função é a quantidade e tipos de argumentos que recebe
