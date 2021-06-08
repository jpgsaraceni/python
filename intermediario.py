"""
DICIONÁRIOS             <dic> = {<chave>: <valor>, <...>}                   // cria dicionário
                        <dic> = dict(<chave>: <valor>)
    ACRESCENTAR CHAVE   <dic>[<nova chave>] = <valor>
    ACESSAR CHAVE       <dic>[<chave>]
    DELETAR CHAVE       del <dic>[<chave>]
    CHECAR CHAVE        if <chave> in <dic>
    ACESSAR VALORES     <dic>.values()
    ACESSAR PARES       <dic.items()
.POP                    <dic>.pop(['<chave>]')
.POPITEM                <dic>.popitem()                                     // corta ultimo item
.UPDATE                 <dic>.update(<dic2>)                                // concatenar
COMPREHENSION           <dic> = {<chave><comando>: <valor><comando> for <chave>, <valor> in <iterável>}
    // iterável deve ter dois valores em cada elemento
***********************************************************************************************************************
FUNÇÕES                 def <fun>(<arg>=<valor padrão>):                    // abre a função. args e valor opcionais
    // quando chamar a função, pode colocar nos parênteses os valores com ou sem <var> = antes.
    // sem os parênteses não executa
RETURN                  return <valor>                                      // termina a função. default = None
*ARGS                   def <fun>(*args):                                   // quando não souber quantos args virão
    // args é por convenção. empacota os argumentos como tupla
**KWARGS                def <fun>(*args, **kwargs):                         // argumentos nomeados (<chave> = <valor>)
LAMBDA                  <var> = (lambda <arg>: <retorno>)                   // cria uma função na declaração
.GET                    <var> = kwargs.get('<chave>')                       // retorna valor recebido para a chave
***********************************************************************************************************************
                        LIST COMPREHENSION
// coloca uma regra na declaração da lista usando for in, referenciando outro iterável
                        <lista> = [<var><op> for <var> in <iter>]
***********************************************************************************************************************
SET                     <set> = {<valores>}                                 // sem repetição e sem índice
.ADD                    <set>.add(<valor>)                                  // acrescenta valor
.DISCARD                <set>.discard(<valor>)
.UPDATE                 <set>.update(<valor>)                               // adiciona da iterado do valor
OPERADORES DE CONJ.     <set>.union(<set2>) ou <set> | <set2>               // união
                        <set> & <set2>                                      // interseção
                        <set> - <set2>                                      // diferença
                        <set> ^ <set2>                                      // AUB - A int B
COMPREHENSION           <set> = {<var> for <var> in <iter>}
***********************************************************************************************************************
ITERÁVEIS               str, list, set, iter, etc
ITERADORES              retornam um valor de cada vez (pode ser de lista, tupla, etc)
GERADORES               <var> = (<valor> for <valor> in <iterável>)         // só salvam um valor na memória
NEXT                    next(<iterável)                                     // retorna o próximo valor
                        // os valores utilizados em iteradores e geradores são consumidos.
***********************************************************************************************************************
MÓDULOS                 from <arquivo> import <dados>                       // para um dado
ctrl + espaço (depois do import) mostra tudo que há no módulo
                        import <mod>                                        // para o modulo todo
                        from <mod> import *                                 // importa tudo, não precisa escrever <mod>.
                                                                                <dado> para acessar.
<mod>. mostra tudo do módulo também
<mod>.<dado>            precisa dessa sintaxe para executar comando, não pode diretamente se importar tudo
from <mod> import <dado> as <nome>                                          // muda o nome nesse código
from itertools import
COUNT
from functools import
REDUCE                  reduce(<func>, <iterável>, <val inicial>)           // acumulador
INSTALAR MOD            pip install <mod>                                   // no terminal
__name__                __name__                                            // retorna o nome do arquivo com relação ao
                                                                                 que está sendo executado (__main__)
***********************************************************************************************************************
RANDOM (MOD)
randint                 random.randint(<de>,<a>)                            // retorna um inteiro aleatório
random                  random()                                            // número entre 0 e 1
***********************************************************************************************************************
FILTER                  filter(<func>: <iterável>)                          // retorna os elementos true
MAP                     map(<func>: <iterável>)
                      // aplica função a cada elemento
***********************************************************************************************************************
TRATAR EXCEÇÕES
                        try:
                            <comandos>
                        except:
                            <comandos>
EXCEPTION               except Exception as <var>:                          // se ocorrer qualquer erro, <var> recebe
                                                                             o erro.
CLASSE DE ERRO          except <classe erro> as <var>:                     // manda para a <var> caso aquele erro ocorra
ELSE                                                                        // executado se não ocorrer erro
FINALLY                 finally:
                            <comando>                                       // sempre executa
RAISE                                                                       // relança exceção tratada
                        raise <exceção>("<mensagem">)                       // se ocorrer o erro, aparece o erro c mens

***********************************************************************************************************************
PACOTES                 // Diretório contendo arquivo __init__.py
acessar mod             <pac>.<mod>.<dado>
    from <pac>.<mod> import <dado>
***********************************************************************************************************************
ARQUIVOS

"""
# revisar itertools
