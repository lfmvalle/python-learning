"""
******************************
Calculadora simples-até-demais
******************************

Esse simples programa pede ao usuário 2 números inteiros e positivos, sendo que o segundo número não pode ser zero.
Com estes dois números, as operações de adição, subtração, multiplicação, divisão e potenciação são realizadas.
Os resultados são realizados dentro de uma função, que retorna todas as operações em uma tupla.
A tupla é descompactada em variáveis-resultado, e essas variáveis são chamadas em um bloco de resultados formatado.

É um exercício simples de lógica básica, realizado para fins de treinamento, usando as noções de:
-> variáveis e conversão de tipagem ('string', 'integer', 'float')
-> operações lógicas (if, else, and)
-> operações binárias (+, *, etc.)
-> formatação de 'strings'
-> laços (while)
-> tuplas e desempacotamento de tuplas
-> definição de funções e funções lambda
-> importar funções
"""


import os  # importa a biblioteca 'os', Operational System, que trabalha com funções que o sistema usa
from math import pow  # da biblioteca 'math', importe a função 'pow' (função que calcula potenciação)

# defino aqui uma função-lambda limpar o que foi exibido no terminal
clr = lambda: os.system('clear')

# defino aqui outra função-lambda que irá exibir um 'cabeçalho' para ser exibido quantas vezes for necessário
hdr_show = lambda: print('*' * 30 + '\nCALCULADORA SIMPLES-ATÉ-DEMAIS\n' + '*' * 30
                         + '\n\nDigite "q" para sair a qualquer momento.\n' + '-' * 40)


def calc(a, b):  # define a função 'calc' com dependência de dois parâmetros: 'a' e 'b'
    return a + b, a - b, a * b, a / b, a // b, a % b, int(pow(a, b))  # a função retorna uma tupla das operações


hdr_show()  # exibe o cabeçalho inicial

"""
O bloco a seguir ('while True', ou como eu gosto de chamar, 'enquanto eu quiser!') é ideal para que o programador
    mantenha o usuário preso em um loop infinito, até que o usuário atinja uma condição específica que o programador
    exija.
No exemplo deste próprio programa, o usuário deve digitar dois números ('n1' e 'n2'), que devem ser inteiros, positivos
    e, para o caso de 'n2', diferente de zero. Se o usuário digitar qualquer outra coisa no lugar disso, ele irá quebrar
    o programa. Então, o bloco 'enquanto eu quiser!' irá verificar as condições necessárias para que o programa não seja
    quebrado. Somente quando estas condições forem satisfeitas, o programa sairá do laço. De outra forma, ele exibirá
    erros na tela e pedirá indefinidamente ao usuário para digitar os números de forma adequada.
É importante, no entanto, fornecer uma 'saída' para o usuário além de forçá-lo a matar o processo. Dentro do laço, será
    definido um termo para que o usuário saia do programa. Neste caso, eu defino a letra 'q' (de 'quit') para que
    o usuário possa sair do programa sem precisar empreender trabalho adicional para matá-lo forçadamente.
"""

while True:  # enquanto eu quiser!
    n1 = input('Digite um número inteiro positivo: ')  # pede ao usuário o primeiro número inteiro (n1)
    if n1 == 'q':  # se o usuário digitar 'q', então:
        quit()  # encerra o programa
    n2 = input('Digite outro número inteiro positivo (diferente de zero): ')  # pede o segundo número inteiro (n2)
    if n2 == 'q':  # se o usuário digitar 'q', então:
        quit()  # encerra o programa

    if n2 == '0':  # se 'n2' for igual a zero, então exibe uma mensagem de erro
        clr()  # limpa o terminal antes de imprimir o erro, para evitar poluição de tela
        hdr_show()  # exibe o cabeçalho novamente
        print(f'Por favor, digite um número inteiro diferente de zero para o segundo número.\n\n---\n')
        continue  # e retorna ao início do laço while (até que 'n2' não seja zero)
    else:  # caso contrário, se 'n2' não for igual a zero, então:
        if n1.isdigit() and n2.isdigit():  # se 'n1' e 'n2' forem dígitos (necessariamente inteiros), então:
            n1, n2 = int(n1), int(n2)  # altera a tipagem de 'n1' e 'n2' de string para integer
            break  # encerra o laço while
        else:  # caso contrário, se 'n1' e 'n2' não forem dígitos, então exibe uma mensagem de erro:
            clr()  # limpa o terminal antes de imprimir o erro, para evitar poluição da tela
            hdr_show()  # exibe o cabeçalho novamente
            print('Você não digitou número(s) inteiro(s) positivo(s). Tente novamente.\n\n---\n')


# O retorno da função 'calc' é uma tupla que será descompactada e atribuída às variáveis 'sum_ab' ... 'pow_ab'
sum_ab, minus_ab, mult_ab, ex_div_ab, div_ab, mod_ab, pow_ab = calc(n1, n2)

# exibe o bloco de resultados
print('-' * 48 + f'\nThe sum of {n1} and {n2} is: {sum_ab}\n'  # exibe a soma entre 'n1' e 'n2'
                 f'The subtraction of {n2} from {n1} is: {minus_ab}\n'  # exibe a subtração
                 f'The product between {n1} and {n2} is: {mult_ab}\n'  # exibe a multiplicação
                 f'The number {n1} divided by the number {n2} is: {div_ab}\n'  # exibe a divisão
                 f'The modulus from {n1} divided by {n2} is: {mod_ab}\n'  # exibe o resto da divisão
                 f'Thus, the exact division of {n1} by {n2} is: {ex_div_ab:.3f}\n'  # exibe a divisão exata
                 f'The {n1} to the power of {n2} is: {pow_ab}\n' + '-' * 48)  # exibe a potenciação
