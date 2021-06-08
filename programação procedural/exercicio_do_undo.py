def exibir(lista):
    print(f' \nLista de tarefas:')
    for a in lista:
        print(a)
    print()


def redo_undo(apagar_de, acrescentar_em):
    if not apagar_de:
        print('Opção inválida.')
        pass
    else:
        acrescentar_em.append(apagar_de[-1])
        apagar_de.pop()


def nova_tarefa(lista):
    tarefa = input('Digite uma nova tarefa:')
    lista.append(tarefa)


to_do = []
redo = []

nova_tarefa(to_do)
exibir(to_do)

while True:
    print('Digite o comando desejado:')
    opcao = input(f'1 - Adicionar Tarefa\n2 - Exibir Lista\n3 - Desfazer\n4 - Refazer\n5 - Encerrar\n')

    if opcao == '1':
        nova_tarefa(to_do)
    elif opcao == '2':
        exibir(to_do)
    elif opcao == '3':
        redo_undo(to_do, redo)
    elif opcao == '4':
        redo_undo(redo, to_do)
    elif opcao == '5':
        break
    else:
        print('Comando inválido! Tente novamente.')

print('Tchau!')
