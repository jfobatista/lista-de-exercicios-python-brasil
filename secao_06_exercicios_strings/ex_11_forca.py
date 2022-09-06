"""
    Exercício 11 da seção de Strings da Python Brasil:
    https://wiki.python.org.br/ExerciciosComStrings

    Desenvolva um jogo da forca. O programa terá uma palavra a qual o jogador deverá acertar em até 6 erros antes de ser enforcado.

    >>> from secao_06_exercicios_strings import ex_11_forca
    >>> letra = ['P', 'O','Y','A','Z','T','H','I','N','R', 'PYTHON']
    >>> ex_11_forca.input = lambda k: letra.pop()
    >>> ex_11_forca.jogo_da_forca()
    Digite uma letra: R
    -> Você errou pela 1 vez. Tente de novo!
    Digite uma letra: N
    _ _ _ _ _ N
    Digite uma letra: I
    -> Você errou pela 2 vez. Tente de novo!
    Digite uma letra: H
    _ _ _ H _ N
    Digite uma letra: T
    _ _ T H _ N
    Digite uma letra: Z
    -> Você errou pela 3 vez. Tente de novo!
    Digite uma letra: A
    -> Você errou pela 4 vez. Tente de novo!
    Digite uma letra: Y
    _ Y T H _ N
    Digite uma letra: O
    _ Y T H O N
    Digite uma letra: P
    P Y T H O N

    Parabéns, você ganhou!

"""


def jogo_da_forca():
    palavra = str(input('Digite a palavra a ser descoberta:')).upper()

    conjunto_letras_palavra = set(palavra)
    conjunto_letras_digitadas = set()
    erros = 0

    while (not conjunto_letras_palavra.issubset(conjunto_letras_digitadas)) and erros < 7:

        letra_digitada = input('Digite uma letra: ').upper()
        print(f'Digite uma letra: {letra_digitada}')
        conjunto_letras_digitadas.add(letra_digitada)
        if letra_digitada in conjunto_letras_palavra:
            for letra in palavra:
                if letra in conjunto_letras_digitadas:
                    print(f'{letra} ', end='')
                else:
                    print('_ ', end='')
            print('')
        else:
            erros += 1
            print(f'-> Você errou pela {erros} vez. Tente de novo!')

    if erros < 7:
        print('Parabéns, você ganhou!')
    else:
        print('Infelizmente você perdeu.')
