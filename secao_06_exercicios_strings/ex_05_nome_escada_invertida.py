"""
    Exercício 05 da seção de Strings da Python Brasil:
    https://wiki.python.org.br/ExerciciosComStrings

     Faça um programa que solicite o nome do usuário e imprima-o na vertical em escada invertida.

    >>> nome_na_vertical_em_escada('joao')
    joao
    joa
    jo
    j

"""


def nome_na_vertical_em_escada(nome):
    for i in range(len(nome)):
        for j in range(0, len(nome) - i):
            print(nome[j], end='')
        print()
