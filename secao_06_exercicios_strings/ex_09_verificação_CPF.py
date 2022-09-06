"""
    Exercício 09 da seção de Strings da Python Brasil:
    https://wiki.python.org.br/ExerciciosComStrings

    Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um
    número válido ou inválido.

    >>> validacao_de_cpf('529.982.247-25')
    'CPF Válido'
    >>> validacao_de_cpf('416.405.668-77')
    'CPF Inválido'
    >>> validacao_de_cpf('416.406.668-77')
    'CPF Válido'
    >>> validacao_de_cpf('090.531.528-65')
    'CPF Válido'
    >>> validacao_de_cpf('090.531.527-64')
    'CPF Inválido'


"""


def calculo_verificacao(primeiros_digitos, multiplicador, digito):
    resultado = 0
    for i in primeiros_digitos:
        resultado += (int(i) * multiplicador)
        multiplicador -= 1

    if digito == 1:
        primeiro_digito = (resultado * 10) % 11
        return primeiro_digito

    return resultado, multiplicador


def validacao_de_cpf(cpf):
    cpf = cpf.split('-')
    primeira_parte = cpf[0]
    segunda_parte = cpf[1]
    primeira_parte = ''.join(primeira_parte.split('.'))

    primeiro_digito_validador = int(segunda_parte[0])
    segundo_digito_validador = int(segunda_parte[1])

    valida_primeiro_digito = calculo_verificacao(primeira_parte, multiplicador=10, digito=1)

    if not valida_primeiro_digito == primeiro_digito_validador:
        return 'CPF Inválido'

    valida_segundo_digito, multiplicador = calculo_verificacao(primeira_parte, multiplicador=11, digito=2)

    valida_segundo_digito += (primeiro_digito_validador * multiplicador)
    valida_segundo_digito = valida_segundo_digito * 10 % 11

    if not valida_segundo_digito == segundo_digito_validador:
        return 'CPF Inválido'

    return 'CPF Válido'
