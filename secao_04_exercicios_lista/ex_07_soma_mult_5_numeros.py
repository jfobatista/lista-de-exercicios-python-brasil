"""
Exercício 07 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

    >>> calcular_numeros(7, 7, 7, 7, 8)
    A soma dos números (7, 7, 7, 7, 8) é: 36 e a multiplicação deles é: 19208


"""


def calcular_numeros(*numeros):
    soma = 0
    multiplicacao = 1
    for i in numeros:
        soma += i
        multiplicacao *= i

    print(f'A soma dos números {numeros} é: {soma} e a multiplicação deles é: {multiplicacao}')
