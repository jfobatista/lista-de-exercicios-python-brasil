"""
    Exercício 19 da seção de listas da Python Brasil:
    https://wiki.python.org.br/ExerciciosListas

    Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:

    "Qual o melhor Sistema Operacional para uso em servidores?"

    As possíveis respostas são:

    1- Windows Server
    2- Unix
    3- Linux
    4- Netware
    5- Mac OS
    6- Outro
    Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma.
    O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos
    valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor.
    Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar
    o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

    Sistema Operacional     Votos   %
    -------------------     -----   ---
    Windows Server           1500   17%
    Unix                     3500   40%
    Linux                    3000   34%
    Netware                   500    5%
    Mac OS                    150    2%
    Outro                     150    2%
    -------------------     -----
    Total                    8800

    O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

    >>> from secao_04_exercicios_lista import ex_19_enquete_SO
    >>> entradas = ['0','1', '1','2','2','25','2','5','6','3','1','2','4']
    >>> ex_19_enquete_SO.input = lambda k: entradas.pop()
    >>> ex_19_enquete_SO.enquete_so()

"""

def enquete_so():
    sistemas = ['Windows Server','Unix','Linux','Netware','Mac OS','Outro']
    votos = [0] * 6
    voto_so = int(input('Informe qual SO você prefere (0 = fim): '))

    while voto_so > 0:
        if not (1 <= voto_so <= 6):
            print('Informe um valor entre 1 e 6 ou 0 para sair!')
        else:
            votos[voto_so-1] += 1
        voto_so = int(input('Informe qual SO você prefere (0 = fim): '))

    num_votos = 0
    for i in votos:
        num_votos += i
    print('Sistema Operacional   Votos   %')

    for indice, item in enumerate(sistemas):
        print(f'{item:<22} {votos[indice]:<5} {votos[indice] / num_votos:>3.0%}')
    print(f'Total {num_votos:>19}')
    melhor_votado = sistemas[votos.index(max(votos))]
    print(f'O melhor jogador foi o número {melhor_votado}, com {(max(votos))} votos, correspondendo a {votos[votos.index(max(votos))] / num_votos:.0%} do total de votos.')