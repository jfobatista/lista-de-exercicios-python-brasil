"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""
from math import ceil, floor


def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
    area_a_ser_pintada = int(input('Informe a área a ser pintada: '))
    area_a_ser_pintada = area_a_ser_pintada * 1.1
    quantidade_de_litros = ceil(area_a_ser_pintada / 6)
    quantidade_de_latas = ceil(quantidade_de_litros / 18)
    quantidade_de_galoes = ceil(quantidade_de_litros / 3.6)
    custo_em_latas = quantidade_de_latas * 80
    custo_em_galoes = quantidade_de_galoes * 25
    litros_excedentes_latas = (18 * quantidade_de_latas) - quantidade_de_litros
    litros_excedentes_galoes = (3.6 * quantidade_de_galoes) - quantidade_de_litros
    quantidade_latas_misturado = floor(quantidade_de_litros / 18)
    quantidade_galoes_misturado = ceil((quantidade_de_litros - (quantidade_latas_misturado * 18)) / 3.6)
    menor_custo = (quantidade_galoes_misturado * 25) + (quantidade_latas_misturado * 80)
    litros_excedentes_misturado = ((quantidade_latas_misturado * 18) + (quantidade_galoes_misturado * 3.6)) - quantidade_de_litros

    print(f'Você deve comprar {quantidade_de_litros} litros de tinta.')
    print(
        f'Você pode comprar {quantidade_de_latas} lata(s) de 18 litros a um custo de R$ {custo_em_latas}. Vão sobrar {litros_excedentes_latas:.1f} litro(s) de tinta.')
    print(
        f'Você pode comprar {quantidade_de_galoes} lata(s) de 3.6 litros a um custo de R$ {custo_em_galoes}. Vão sobrar {litros_excedentes_galoes:.1f} litro(s) de tinta.')
    print(
        f'Para menor custo, você pode comprar {quantidade_latas_misturado} lata(s) de 18 litros e {quantidade_galoes_misturado} galão(ões) de 3.6 litros a um custo de R$ {menor_custo}. Vão sobrar {litros_excedentes_misturado:.1f} litro(s) de tinta.')
