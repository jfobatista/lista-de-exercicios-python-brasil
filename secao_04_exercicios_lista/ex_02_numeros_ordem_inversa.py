"""
Exercício 02 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

    >>> ler_10_valores_ordem_inversa(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    10
    9
    8
    7
    6
    5
    4
    3
    2
    1

"""


def ler_10_valores_ordem_inversa(*numeros):
    """Escreva aqui em baixo a sua solução"""
    numeros = reversed(numeros)

    for i in numeros:
        print(i)