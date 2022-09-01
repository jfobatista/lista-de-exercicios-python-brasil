"""
Exercício 01 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosComStrings

Tamanho de strings. Faça um programa que compare 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings

String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.

    >>> comparar('Brasil Hexa 2006', 'Brasil! Hexa 2006!')
    String 1: Brasil Hexa 2006
    String 2: Brasil! Hexa 2006!
    Tamanho de "Brasil Hexa 2006": 16 caracteres
    Tamanho de "Brasil! Hexa 2006!": 18 caracteres
    As duas strings são de tamanhos diferentes.
    As duas strings possuem conteúdo diferente.

"""


def comparar(s1: str, s2: str):
    """Escreva aqui em baixo a sua solução"""
    if s1 != s2:
        print(f'String 1: {s1}')
        print(f'String 2: {s2}')
        print(f'Tamanho de "{s1}": {len(s1)} caracteres')
        print(f'Tamanho de "{s2}": {len(s2)} caracteres')
        print(f'As duas strings são de tamanhos diferentes.')
        print(f'As duas strings possuem conteúdo diferente.')
    else:
        print(f'String 1: {s1}')
        print(f'String 2: {s2}')
        print(f'Tamanho de {s1}: {len(s1)} caracteres')
        print(f'Tamanho de {s1}: {len(s2)} caracteres')
        print(f'As duas strings são de tamanhos iguais.')
        print(f'As duas strings possuem o mesmo conteúdo.')
