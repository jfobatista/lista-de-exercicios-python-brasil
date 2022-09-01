"""
    Exercício 04 da seção de Strings da Python Brasil:
    https://wiki.python.org.br/ExerciciosComStrings

     Faça um programa que solicite o nome do usuário e imprima-o na vertical em escada.

    >>> nome_na_vertical_em_escada('joao')
    j
    jo
    joa
    joao

"""


def nome_na_vertical_em_escada(nome):
    for i in range(len(nome)):
        for j in range(0, i + 1):
            print(nome[j], end='')
        print()
