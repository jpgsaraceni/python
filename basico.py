"""
************************************************************************************************************************
INPUT:          <var> = input(<mensagem>)                   // escreve a mensagem e recebe digitado
************************************************************************************************************************
PRINT           print(<var> ou <str> ou <int>)              // aceita diversos tipos
SEP             print(<conteúdo>, sep=<caractere>)          // como separar os valores
END             print(<conteúdo>, end=<caractere>)          // o que acontece ao final
+               print(<conteúdo> + <conteúdo>)              // concatena
*               print(<conteúdo> * <n>)                     // repete n vezes
OR              print(<var1> or <var2>)                     // imprime primeiro true
************************************************************************************************************************
F_STRINGS       print(f'<texto> {<var>} <texto>')           // variável entre chaves
:<car><op><n>   print(f'{<var>:<car><op><n>}')              // n caracteres total, <>^ posição
:s              print(f'{<var>:s}')                         // string
:d              print(f'{<var>:d}')                         // inteiro
:f              print(f'{<var>:f}')                         // float
:.<n>f          print(f'{<var:.<n>f}')                      // aproxima n casas
************************************************************************************************************************
                STRINGS
<var>.<fun>     para formatar a variável
.FORMAT         print('{:<car><op><n>}'.format(<var>))      // string vira comando
                                                            // se colocar chave vazia na str, preenche com var
ÍNDICE          print('{<n>}'.format(<var0>, <var1>, <...>) // acessa var índice n no format
.UPPER          print(<var>.upper())                        // maiúsculas
.LOWER                                                      // minúsculas
.ISDIGIT        <var>.isdigit()                             // checa se pode ser transformado em inteiro
\                                                           // ignora o próximo comando
\n                                                          // quebra linha
r_strings       print(r'\n \n \n`)                          // ignora todos os comandos dentro da string
.STARTSWITH     <str>.startswith(<prefixo>)                 // checa se tem o prefixo no começo
.SPLIT          <str>.split(<caractere>)                    // divide em listas no caractere entre parenteses
.COUNT          <var>.count('<car>')                        // retorna quantas vezes o caractere aparece na str
.JOIN           '<car>'.join(<var>)                         // junta iterável em uma str, separando com o caractere
************************************************************************************************************************
CONDICIONAIS    if <condição>:                              // indentação de 4 espaços cria bloco
                else:
                elif:
                pass
                ...
************************************************************************************************************************
RELACIONAIS     ==, >, <, <=, >=, !=
LÓGICOS         and, or, not, in, not in
************************************************************************************************************************
TYPE            type(<var>)                                 // retorna o tipo de variável
CASTING         <tipo>(<var>)                               // converte a variável para o tipo
************************************************************************************************************************
OP ARITMÉTICOS  +, -, *, /
                // divisão inteira arredondada
                ** exponenciação
                % módulo (resto)
                ()
************************************************************************************************************************
LEN             len(<var>)                                  // retorna número de iteráveis
************************************************************************************************************************
ÍNDICE          <var>[<n>]                                  // elemento de índice n. se <0, conta do último
FATIAMENTO      <var>[<n1>:<n2>]                            // inclui n1 exclui n2
                                                            // sem n1 do início, sem n2 até o fim
    ]PASSO      <var>[<inicio>:<fim>:<passo>]
.STRIP          <var>.strip()                               // remove espaço no início e fim
.REPLACE        <var>.replace(<sai>,<entra>)                // substitui caracteres
************************************************************************************************************************
LISTAS          <var> = [<var1>, <var2>]                    // <var1> é índice 0, etc.
                                                            // contém qualquer tipo de dado
CONCATENAR      <lista> + <lista>
                <lista>.extend(<var>)                       // para iteráveis
                <lista>.append(<var>)                       // para objetos do mesmo tipo
INSERIR         <lista>.insert(<i>, <v>)                    // insere v no índice i
POP             <lista>.pop()                               // apaga o último elemento
DEL             del <lista>[<intervalo>]                    // apaga os termos
MAX             max(<lista>)                                // maior valor
MIN             min(<lista>)                                // menor valor
DESEMPACOTAR    <var1>, <var2> = lista                      // cada variável recebe um valor
*               <var1>, *<var2>, <var3> = lista             // *var2 pega os valores que sobram e cria uma lista
                *<lista>                                    // desempacota a lista
*_              <v1>, <v2>, *_                              // usado por convenção p descartar valores
ENUMERATE       enumerate(lista)                            // cria tuplas com índice e valor da lista
.SORT           <lista>.sort()                              // ordena os elementos
    KEY         .sort(key=<fun>)                            // ordena segundo os elementos retornados pela função
.SORTED         <lista>.sorted()                            // ordena sem alterar a lista na memória
************************************************************************************************************************
RANGE           range(<start>, <stop>)                      // cria sequência de inteiros no intervalo
FOR IN          for <valor> in <iterável>:                  // passa por cada elemento do iterável
CONTINUE        continue                                    // passa para o próximo laço
BREAK           break                                       // quebra a iteração
WHILE           while <condição>:                           // enquanto verdadeiro executa laço
ELSE            else:                                       // pode ser usado em for e while
************************************************************************************************************************
TUPLA           <tupla> = (<v1>, <v2>)                      // elementos não podem ser alterados
************************************************************************************************************************
VARIÁVEIS       <var> = <valor>                             // começar com letra, separar por _, somente minúsculas
TROCAR VALOR    <v1>, <v2> = <v2>, <v1>                     // trocam
OP TERNÁRIO     <var> = <valor> if <cond> else <v2>         // faz if else na mesma linha
                <v1> = <condição>
                <v2> = <v3> if <v1> else <v4>               // retorna v3 se condição verdadeira
CONSTANTE       <VAR> = <valor>                             // usar maiusculas para cosntante
"""
a = 2
b = '{:0>14}'.format(a)
print(b, type(b))
