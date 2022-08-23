"""
Exercício 05 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os
números IMPARES no vetor impar. Imprima os três vetores.

    >>> imprimir_vetor_pares_e_impares(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
    Números: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    Pares: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    Ímpares: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

"""


def imprimir_vetor_pares_e_impares(*numeros):
    """Escreva aqui em baixo a sua solução"""
    vetor_numeros = []
    vetor_pares = []
    vetor_impares = []
    for i in numeros:
        vetor_numeros.append(i)
        if i % 2 == 0:
            vetor_pares.append(i)
        else:
            vetor_impares.append(i)
    print(f'Números: {vetor_numeros}')
    print(f'Pares: {vetor_pares}')
    print(f'Ímpares: {vetor_impares}')
