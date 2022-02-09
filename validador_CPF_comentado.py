"""
Validador de CPF
"""

while True:  # enquanto verdadeiro
    cpf_completo = input('Digite o número CPF a ser verificado (apenas números):\n')  # pede ao usuário para digitar um número CPF

    if cpf_completo.isnumeric() and len(cpf_completo) == 11:  # se o valor digitado pelo usuário é um número inteiro E tem 11 algarismos:
        break  # sai do loop while
    else:  # caso contrário
        print(f'O número CPF digitado ({cpf_completo}) não é válido.\nVerifique o número e tente novamente.\n----------')  # informa que o valor digitado não é válido e repete o loop while

cpf = cpf_completo[:-2]  # variável 'cpf' recebe os 9 dígitos iniciais do valor digitado pelo usuário (excluindo os dígitos verificadores)

# informa na tela o número CPF a ser verificado, e seus dígitos verificadores
print(f'----------\nO CPF a ser verificado é: {cpf}\nPrimeiro dígito verificador: {cpf_completo[-2]}\nSegundo dígito verificador: {cpf_completo[-1]}\n\nVerificando...\n')

d1 = 0  # variável 'dígito verificador 1'
soma = 0  # variável 'soma'

for i, j in enumerate(range(10, 1, -1)):  # para 'i' e 'j', enumera 'i' a partir de 0 para cada 'j' entre 10 e 2, diminuindo 1 do valor de j a cada passo do loop for
    soma += int(cpf[i]) * j  # variável 'soma' recebe o valor anterior acrescido do algarismo atual do cpf multiplicado pelo valor atual de j
d1 = 11 - (soma % 11)  # valor do 'dígito verificador 1' é calculado
if d1 > 9:  # se o valor do 'dígito verificador 1' é maior que 9:
    d1 = 0  # 'd1' recebe o valor 0
print(f'Número calculado para o primeiro dígito verificador: {d1}')  # informa na tela o valor calculado para o primeiro dígito verificador

d2 = 0  # variável 'dígito verificador 2'
soma = 0  # variável 'soma' recebe o valor 0 para ser usada novamente
cpf_d1 = cpf + str(d1)  # variável cpf_d1 é o valor 'cpf' + 'dígito verificador 1', calculado no loop anterior

for i, j in enumerate(range(11, 1, -1)):  # para 'i' e 'j', enumera 'i' a partir de 0 para cada 'j' entre 11 e 2, diminuindo 1 do valor de j a cada passo do loop for
    soma += int(cpf_d1[i]) * j  # variável 'soma' recebe o valor anterior acrescido do algarismo atual do cpf multiplicado pelo valor atual de j
d2 = 11 - (soma % 11)  # valor do 'dígito verificador 2' é calculado
if d2 > 9:  # se o valor do 'dígito verificador 2' é maior que 9:
    d2 = 0  # 'd2' recebe o valor 0
print(f'Número calculado para o segundo dígito verificador: {d2}')  # informa na tela o valor calculado para o primeiro dígito verificador

cpf_d2 = cpf_d1 + str(d2)  # variável cpf_d2 é o valor 'cpf_d1' + 'dígito verificador 2', calculado no loop anterior

# informa na tela se o CPF digitado pelo usuário é válido ou não, comparando o CPF digitado com o CPF de dígito verificador calculado
print('\nCPF digitado é valido.\n----------') if cpf_completo == cpf_d2 else print('\nCPF digitado é inválido.\n----------')
