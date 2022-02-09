"""
Gerador de CPF
"""

from random import randint as rint  # importa a função 'randint' do pacote 'random' como 'rint'

for n in range(5):  # para n entre 0 e 4 (isso gerará 5 CPFs aleatórios)
    while True:  # enquanto verdadeiro:
        cpf = str(rint(100000000, 999999999))  # gera um número aleatório entre 100.000.000 e 999.999.999 para a variável 'cpf'
        if cpf != cpf[0] * 9:  # se o número gerado não é uma sequência (ex: 111.111.111)
            break  # sai do loop while, senão, gera outro número para a variável 'cpf'

    d1 = 0  # variável 'dígito verificador 1'
    soma = 0  # variável 'soma'

    for i, j in enumerate(range(10, 1, -1)):  # para 'i' e 'j', enumera 'i' a partir de 0 p/ cada 'j' entre 10 e 2, diminuindo 1 de 'j' a cada passo do loop
        soma += int(cpf[i]) * j  # variável 'soma' recebe o seu valor anterior somado do novo resultado da multiplicação entre dígito atual da variável 'cpf' pelo atual valor de 'j'
    d1 = 11 - (soma % 11)  # dígito verificador 1 é calculado a partir da variável 'soma'
    if d1 > 9:  # se o número encontrado para a variável 'd1' é maior que 9:
        d1 = 0  # então a variável 'd1' é setada para o valor 0

    d2 = 0  # variável 'dígito verificador 2'
    soma = 0  # reseta o valor da variável 'soma' para ser usada novamente

    cpf_d1 = cpf + str(d1)  # variável 'cpf_d1' é a variável 'cpf' gerada aleatoriamente + dígito verificador 1

    for i, j in enumerate(range(11, 1, -1)):  # para 'i' e 'j', enumera 'i' a partir de 0 p/ cada 'j' entre 11 e 2, diminuindo 1 de 'j' a cada passo do loop
        soma += int(cpf_d1[i]) * j  # variável 'soma' recebe o seu valor anterior somado do novo resultado da multiplicação entre dígito atual da variável 'cpf' pelo atual valor de 'j'
    d2 = 11 - (soma % 11)  # dígito verificador 2 é calculado a partir da variável 'soma'
    if d2 > 9:  # se o número encontrado para a variável 'd1' é maior que 9:
        d2 = 0  # então a variável 'd1' é setada para o valor 0

    cpf_d2 = cpf_d1 + str(d2)  # variável 'cpf_d2' é a variável 'cpf_d1' + dígito verificador 2

    print(f'CPF {n+1}:\t{cpf_d2}')  # retorna o número CPF 'n' gerado aleatoriamente com dígito verificador validado
