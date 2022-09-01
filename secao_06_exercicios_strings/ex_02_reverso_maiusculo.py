"""
    Exercício 02 da seção de Strings da Python Brasil:
    https://wiki.python.org.br/ExerciciosComStrings

    Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.

    >>> nome_ao_contrario_maiusculo('joao')
    OAOJ

"""


def nome_ao_contrario_maiusculo(nome):
    nome = nome.upper()
    for character in reversed(nome):
        print(character, end="")
