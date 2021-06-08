# print(<int> ou <'sting'>)
print('por padrão, já imprime espaço quando separar argumentos por', 'vírgula')
# se colocar ao final da função print um <sep='<string>' irá separar os argumentos usando essa string.
print('fazer', 'isso', 'para', 'separar', 'com', 'traços', sep='-')
# end=<o que fazer no final da linha>
print('assim fica colado na próxima', end='')
print('linha')

# imprimir cpf com formatação
print(123, 456, 789, sep='.', end='-')
print('00')

print('texto' + 'texto')  # +com string é concatenar
print(10 * 'texto')  # *com string repete

print(0 or False or 'oi' or 'tchau')  # or procura o primeiro valor
