"""
Exercício 03 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

    >>> ler_4_notas(7, 8, 9, 10)
    7
    8
    9
    10
    8.5
    >>> ler_4_notas(10, 10, 10, 10)
    10
    10
    10
    10
    10.0

"""


def ler_4_notas(*notas):
    """Escreva aqui em baixo a sua solução"""
    soma_das_notas = numero_de_notas = 0
    for i in notas:
        soma_das_notas += i
        numero_de_notas += 1
        print(i)
    print(soma_das_notas/numero_de_notas)
