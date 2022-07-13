"""
Exercício 19 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

    >>> decompor_numero(1000)
    'O número precisa ser menor que 1000'
    >>> decompor_numero(-1)
    'O número precisa ser positivo'
    >>> decompor_numero(326)
    '326 = 3 centenas, 2 dezenas e 6 unidades'
    >>> decompor_numero(300)
    '300 = 3 centenas'
    >>> decompor_numero(100)
    '100 = 1 centena'
    >>> decompor_numero(320)
    '320 = 3 centenas e 2 dezenas'
    >>> decompor_numero(310)
    '310 = 3 centenas e 1 dezena'
    >>> decompor_numero(305)
    '305 = 3 centenas e 5 unidades'
    >>> decompor_numero(301)
    '301 = 3 centenas e 1 unidade'
    >>> decompor_numero(311)
    '311 = 3 centenas, 1 dezena e 1 unidade'
    >>> decompor_numero(111)
    '111 = 1 centena, 1 dezena e 1 unidade'
    >>> decompor_numero(101)
    '101 = 1 centena e 1 unidade'
    >>> decompor_numero(25)
    '25 = 2 dezenas e 5 unidades'
    >>> decompor_numero(20)
    '20 = 2 dezenas'
    >>> decompor_numero(21)
    '21 = 2 dezenas e 1 unidade'
    >>> decompor_numero(10)
    '10 = 1 dezena'
    >>> decompor_numero(16)
    '16 = 1 dezena e 6 unidades'
    >>> decompor_numero(1)
    '1 = 1 unidade'
    >>> decompor_numero(7)
    '7 = 7 unidades'

"""
from math import floor


def decompor_numero(numero: int):
    """Escreva aqui em baixo a sua solução"""
    centenas = floor(numero / 100)
    dezenas = floor((numero - centenas * 100) / 10)
    unidades = floor(numero - (centenas * 100) - (dezenas * 10))

    if numero >= 1000:
        return 'O número precisa ser menor que 1000'
    if numero < 0:
        return 'O número precisa ser positivo'

    if centenas > 1 and dezenas > 1 and unidades > 1:
        numero_text = f'{numero} = {centenas} centenas, {dezenas} dezenas e {unidades} unidades'
    elif centenas > 1:
        if dezenas == 0:
            if unidades == 1:
                numero_text = f'{numero} = {centenas} centenas e {unidades} unidade'
            elif unidades > 1:
                numero_text = f'{numero} = {centenas} centenas e {unidades} unidades'
            else:
                numero_text = f'{numero} = {centenas} centenas'
        elif dezenas > 1:
            if unidades > 1:
                numero_text = f'{numero} = {centenas} centenas, {dezenas} dezenas e {unidades} unidades'
            elif unidades == 1:
                numero_text = f'{numero} = {centenas} centenas, {dezenas} dezenas e {unidades} unidade'
            else:
                numero_text = f'{numero} = {centenas} centenas e {dezenas} dezenas'
        elif dezenas == 1:
            if unidades == 1:
                numero_text = f'{numero} = {centenas} centenas, {dezenas} dezena e {unidades} unidade'
            elif unidades > 1:
                numero_text = f'{numero} = {centenas} centenas, {dezenas} dezena e {unidades} unidades'
            else:
                numero_text = f'{numero} = {centenas} centenas e {dezenas} dezena'
    elif centenas == 1:
        if dezenas == 0:
            if unidades == 1:
                numero_text = f'{numero} = {centenas} centena e {unidades} unidade'
            elif unidades > 1:
                numero_text = f'{numero} = {centenas} centena e {unidades} unidades'
            else:
                numero_text = f'{numero} = {centenas} centena'
        elif dezenas > 1:
            if unidades > 1:
                numero_text = f'{numero} = {centenas} centena, {dezenas} dezenas e {unidades} unidades'
            elif unidades == 1:
                numero_text = f'{numero} = {centenas} centena, {dezenas} dezenas e {unidades} unidade'
            else:
                numero_text = f'{numero} = {centenas} centena e {dezenas} dezenas'
        elif dezenas == 1:
            if unidades == 1:
                numero_text = f'{numero} = {centenas} centena, {dezenas} dezena e {unidades} unidade'
            elif unidades > 1:
                numero_text = f'{numero} = {centenas} centena, {dezenas} dezena e {unidades} unidades'
            else:
                numero_text = f'{numero} = {centenas} centena e {dezenas} dezena'
    elif centenas == 0:
        if dezenas == 0:
            if unidades == 1:
                numero_text = f'{numero} = {unidades} unidade'
            elif unidades > 1:
                numero_text = f'{numero} = {unidades} unidades'
        elif dezenas > 1:
            if unidades > 1:
                numero_text = f'{numero} = {dezenas} dezenas e {unidades} unidades'
            elif unidades == 1:
                numero_text = f'{numero} = {dezenas} dezenas e {unidades} unidade'
            else:
                numero_text = f'{numero} = {dezenas} dezenas'
        elif dezenas == 1:
            if unidades == 1:
                numero_text = f'{numero} = {dezenas} dezena e {unidades} unidade'
            elif unidades > 1:
                numero_text = f'{numero} = {dezenas} dezena e {unidades} unidades'
            else:
                numero_text = f'{numero} = {dezenas} dezena'


        else:
            if unidades == 1:
                numero_text = f'{numero} = {unidades} unidade'
            else:
                numero_text = f'{numero} = {unidades} unidades'

    return numero_text
