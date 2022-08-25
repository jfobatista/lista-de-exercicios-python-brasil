"""
    Exercício 04 da seção de listas da Python Brasil:
    https://wiki.python.org.br/ExerciciosFuncoes

    Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

    >>> positivo_negativo(3)
    'P'

    >>> positivo_negativo(-4)
    'N'
"""


def positivo_negativo(n):
    if n < 0:
        return 'N'

    return 'P'
