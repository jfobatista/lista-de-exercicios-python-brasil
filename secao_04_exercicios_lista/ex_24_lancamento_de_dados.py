"""
Exercício 24 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

A partir de uma simulação de lançamento de dados, foram armazenados os valores de cada lançamento.
Mostre na tela:
1)Quantas vezes o dado foi lançado;
2)Quantas vezes cada valor foi obtido;
3)Qual lado caiu mais vezes (e quantas vezes.)

    >>> lancar_dados(2, 2, 2, 5, 3, 3, 1, 3, 4, 2, 6, 4, 3, 4, 4, 2, 6, 3, 6, 3, 4,
    ... 3, 5, 5, 5, 1, 2, 1, 6, 5, 6, 3, 1, 6, 1, 1, 6, 5, 1, 6, 1, 1, 2, 1, 1, 2, 2,
    ... 4, 4, 4, 2, 1, 4, 6, 6, 4, 2, 4, 4, 2, 5, 3, 6, 1, 2, 5, 4, 4, 5, 3, 4, 6, 6)
    O dado foi lançado 73 vezes
    O número 1 caiu 13 vezes
    O número 2 caiu 13 vezes
    O número 3 caiu 10 vezes
    O número 4 caiu 15 vezes
    O número 5 caiu 9 vezes
    O número 6 caiu 13 vezes
    O lado com o número 4 caiu mais vezes (15 vezes)

    >>> lancar_dados(6, 6, 2, 5, 4, 5, 3, 3, 5, 1, 4, 5, 4, 4, 2, 4, 6, 3, 6, 1,
    ... 6, 6, 6, 6, 5, 5, 6, 6, 3, 5, 5, 1, 5, 5, 5, 2, 6, 4, 5, 5, 1, 3, 2, 3, 3,
    ... 6, 3, 4, 3, 4, 1, 6, 6, 3, 1, 1, 2, 2, 2, 4, 4, 3, 1, 2, 6, 2, 5, 2, 2)
    O dado foi lançado 69 vezes
    O número 1 caiu 8 vezes
    O número 2 caiu 11 vezes
    O número 3 caiu 11 vezes
    O número 4 caiu 10 vezes
    O número 5 caiu 14 vezes
    O número 6 caiu 15 vezes
    O lado com o número 6 caiu mais vezes (15 vezes)

"""


def lancar_dados(*valor_lancamentos):
    """Escreva aqui em baixo a sua solução"""
    lista_rodou = [0, 0, 0, 0, 0, 0]

    for i in valor_lancamentos:
        if i == 1:
            lista_rodou[0] += 1
        if i == 2:
            lista_rodou[1] += 1
        if i == 3:
            lista_rodou[2] += 1
        if i == 4:
            lista_rodou[3] += 1
        if i == 5:
            lista_rodou[4] += 1
        if i == 6:
            lista_rodou[5] += 1
    caiu_mais = numero = 0
    for i in lista_rodou:
        caiu_mais = max(caiu_mais, i)
    print(f'O dado foi lançado {len(valor_lancamentos)} vezes')
    for i, x in enumerate(lista_rodou):
        if x == caiu_mais:
            numero = i + 1
        print(f'O número {i+1} caiu {lista_rodou[i]} vezes')

    print(f'O lado com o número {numero} caiu mais vezes ({caiu_mais} vezes)')
