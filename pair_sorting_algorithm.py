"""
Pair-sorting Algorithm
by @lfmvalle
"""
import random
import time


def pair_sorting(l, crescent=True) -> list:
    """
    Organiza uma dada lista em ordem crescente ou decrescente usando o algoritmo pair-sorting, retornando a lista reorganizada ao final.
    :param list l: Lista com valores de um mesmo tipo (str, int ou float)
    :param bool crescent: Se a organização da lista deve ser em ordem crescente (True, padrão) ou decrescente (False)
    :return: Lista reorganizada
    :rtype: list
    """

    while True:
        last_l = l.copy()
        for i, a in enumerate(l):
            if i < len(l) - 1:
                if crescent and l[i] > l[i + 1]:
                    l[i], l[i + 1] = l[i + 1], l[i]
                    continue
                elif not crescent and l[i] < l[i + 1]:
                    l[i], l[i + 1] = l[i + 1], l[i]
                    continue
        if last_l == l:
            return l


# Testando o algoritmo:
if __name__ == '__main__':
    lst = list(range(1, 5001))  # cria uma lista de 1 a 5000
    random.shuffle(lst)  # embaralha os números da lista
    print(f'Lista inicial: {lst}\n')
    print(f'Reorganizando lista em ordem crescente. Aguarde...')
    time0 = time.perf_counter()
    print(f'Resultado: {pair_sorting(lst.copy())}')
    time1 = time.perf_counter()
    delta_time = round(time1 - time0, 2)
    print(f'Concluiu em {delta_time:.2f} segundos.\n')
    print(f'Reorganizando lista em ordem decrescente. Aguarde...')
    time0 = time.perf_counter()
    print(f'Resultado: {pair_sorting(lst.copy(), crescent=False)}')
    time1 = time.perf_counter()
    delta_time = round(time1 - time0, 2)
    print(f'Concluiu em {delta_time} segundos.')
