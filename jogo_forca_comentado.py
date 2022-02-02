"""
JOGUINHO DE FORCA
> Uma palavra secreta
> 3 chances para errar a letra
> Letras corretas digitadas novamente não consomem chances
> Letras incorretas digitadas novamente consomem chances
"""

palavra = 'guaxinim'  # a palavra secreta que deve ser acertada
digitadas = []  # a lista de letras digitadas corretamente
chances = 3  # número de chances para errar a letra

while True:
    # Verifica o valor de chances restantes. Se zerar, o jogo termina.
    if chances <= 0:
        print(f'Que pena, você perdeu o jogo :(\nA palavra secreta era "{palavra}".')
        break
    # Pede ao usuário para digitar uma letra qualquer
    letra = input('Digite uma letra: ')
    # Verifica se o usuário digitou apenas uma letra
    if len(letra) != 1:
        print('Calma lá: você deve digitar apenas uma letra! :S')
        continue
    # se a letra digitada existe na palavra secreta, então:
    if letra in palavra:
        # se a letra digitada já foi digitada antes (consta na lista de digitadas corretamente), então:
        if letra in digitadas:
            print(f'Você já digitou a letra "{letra}". Digite outra letra!')  # emite um aviso de repetição
        # caso contrário (se a letra não foi digitada antes):
        else:
            digitadas.append(letra)  # adiciona a letra digitada à lista de letras digitadas corretamente
            print(f'Boa! A letra "{letra}" existe na palavra secreta! :)')  # e emite um aviso de acerto
    # caso contrário (se a letra não existe na palavra secreta):
    else:
        print(f'Ops! A letra "{letra}" não existe na palavra secreta! :(')  # emite um aviso de erro
        chances -= 1  # diminui as chances em 1 do valor atual

    temp = ''  # 'temp' será a palavra acertada temporariamente até agora
    # para cada iterável 'n' na palavra secreta:
    for n in palavra:
        # se 'n' consta na lista de letras digitas corretamente:
        if n in digitadas:
            temp += n  # temp recebe o valor de n
        # caso contrário:
        else:
            temp += '*'  # temp recebe o valor de *

    # se a palavra acertada temporariamente corresponder à palavra secreta:
    if temp == palavra:
        print(f'-----\nParabéns! Você ganhou o jogo :)\nA palavra secreta era "{palavra}".')  # emite o aviso de término
        break

    # emite como está a situação atual da palavra e as chances restantes
    print(f'Palavra secreta: {temp}\nChances restantes: {chances}\n-----')
