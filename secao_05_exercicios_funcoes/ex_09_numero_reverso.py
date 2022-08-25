"""
    Exercício 09 da seção de listas da Python Brasil:
    https://wiki.python.org.br/ExerciciosFuncoes

     Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

    >>> numero_reverso(34)
    43

    >>> numero_reverso(214)
    412

    >>> numero_reverso(111)
    111

"""


def numero_reverso(n):
    n_reverso = 0

    while n > 0:
        resto = n % 10
        n_reverso = n_reverso * 10 + resto
        n = n // 10

    return n_reverso