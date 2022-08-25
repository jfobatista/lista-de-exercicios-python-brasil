"""
    Exercício 08 da seção de listas da Python Brasil:
    https://wiki.python.org.br/ExerciciosFuncoes

    Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

    >>> qntdDigitos(34)
    2

    >>> qntdDigitos(1223.214)
    O valor informado não é um inteiro

    >>> qntdDigitos(-122214)
    6

"""


def qntdDigitos(n):
    if not isinstance(n, int):
        print('O valor informado não é um inteiro')
        return
    string = str(n)
    characters = '-'
    string = ''.join(x for x in string if x not in characters)
    return len(string)
