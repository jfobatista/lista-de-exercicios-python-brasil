"""
    Exercício 03 da seção de Strings da Python Brasil:
    https://wiki.python.org.br/ExerciciosComStrings

     Faça um programa que solicite o nome do usuário e imprima-o na vertical.

    >>> nome_na_vertical('joao')
    j
    o
    a
    o

"""


def nome_na_vertical(nome):
    for i in nome:
        print(i)
