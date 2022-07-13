"""
Exercício 09 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre-os em ordem decrescente.

    >>> ordenar_decrescente(2, 3, 5)
    5, 3, 2
    >>> ordenar_decrescente(10, 5.55, 7)
    10, 7, 5.55
    >>> ordenar_decrescente(20, 30, 17.62)
    30, 20, 17.62
    >>> ordenar_decrescente(7, 1, 15)
    15, 7, 1

"""


def ordenar_decrescente(x, y, z):
    """Escreva aqui em baixo a sua solução"""
    maximo = minimo = medio = 0
    if x > y and x > z:
        maximo = x
        if y > z:
            medio = y
            minimo = z
        else:
            medio = z
            minimo = y
    elif y > x and y > z:
        maximo = y
        if x > z:
            medio = x
            minimo = z
        else:
            medio = z
            minimo = x
    elif z > x and z > y:
        maximo = z
        if y > x:
            medio = y
            minimo = x
        else:
            medio = x
            minimo = y

    print(f'{maximo}, {medio}, {minimo}')
