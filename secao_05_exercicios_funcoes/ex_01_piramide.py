"""
    Exercício 01 da seção de listas da Python Brasil:
    https://wiki.python.org.br/ExerciciosFuncoes

    Faça um programa para imprimir:

      1
      2   2
      3   3   3
      .....
      n   n   n   n   n   n  ... n

    para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

    >>> imprime_piramide(3)
    1
    2   2
    3   3   3
    >>> imprime_piramide(4)
    1
    2   2
    3   3   3
    4   4   4   4

"""


def imprime_piramide(n):
    for i in range(1, n + 1):
        for _ in range(i):
            print(f'{i}',end='   ')
        print('')
