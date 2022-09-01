"""
    Exercício 02 da seção de listas da Python Brasil:
    https://wiki.python.org.br/ExerciciosFuncoes

    Faça um programa para imprimir:

      1
      1   2
      1   2   3
      .....
      1   2   3   4   5   n-1  ... n

    para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

    >>> imprime_piramide(3)
    1
    1   2
    1   2   3
    >>> imprime_piramide(4)
    1
    1   2
    1   2   3
    1   2   3   4

"""


def imprime_piramide(n):
    for i in range(1, n + 1):
        for x in range(1, i+1):
            print(f'{x}', end='   ')
        print('')
