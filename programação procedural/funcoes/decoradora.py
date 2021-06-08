def master():
    def slave():    # função principal cria essa
        print('Oi')
    return slave


variavel = master()  # mesmo que variavel = slave
variavel()  # executar slave

################################################


def mestre(funcao):  # função decoradora
    def escravo():
        funcao()
    return escravo


@mestre  # decorador
def fala_oi():
    print('oi')


# variavel = mestre(fala_oi) // não precisa por ter usado @mestre
variavel()
