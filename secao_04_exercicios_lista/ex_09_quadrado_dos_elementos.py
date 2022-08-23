"""
Exercício 09 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

    >>> calcula_quadrado(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    385

"""

def calcula_quadrado(*elementos):
    soma_dos_quadrados = 0
    for i in elementos:
        soma_dos_quadrados += (i**2)

    print(soma_dos_quadrados)