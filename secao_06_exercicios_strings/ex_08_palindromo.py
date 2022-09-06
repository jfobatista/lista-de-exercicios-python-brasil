"""
    Exercício 08 da seção de Strings da Python Brasil:
    https://wiki.python.org.br/ExerciciosComStrings

    Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

    >>> eh_palindromo('OVO')
    'É Palindromo'
    >>> eh_palindromo('OsSo')
    'É Palindromo'
    >>> eh_palindromo('SUBI NO ÔNIBUS')
    'É Palindromo'
    >>> eh_palindromo('Teste')
    'Não é Palindromo'


"""
import unidecode


def eh_palindromo(frase):
    frase = unidecode.unidecode(frase).lower()
    frase = frase.split(' ')
    frase = ''.join(frase)
    frase_invertida = ''

    for character in reversed(frase):
        frase_invertida += character

    if frase == frase_invertida:
        return 'É Palindromo'

    return 'Não é Palindromo'
