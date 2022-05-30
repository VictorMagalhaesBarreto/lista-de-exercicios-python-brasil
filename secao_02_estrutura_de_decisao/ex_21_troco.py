"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.

    >>> calcular_troco(256)
    '2 notas de R$ 100, 1 nota de R$ 50, 1 nota de R$ 5 e 1 nota de R$ 1'
    >>> calcular_troco(1)
    '1 nota de R$ 1'
    >>> calcular_troco(5)
    '1 nota de R$ 5'
    >>> calcular_troco(10)
    '1 nota de R$ 10'
    >>> calcular_troco(11)
    '1 nota de R$ 10 e 1 nota de R$ 1'
    >>> calcular_troco(399)
    '3 notas de R$ 100, 1 nota de R$ 50, 4 notas de R$ 10, 1 nota de R$ 5 e 4 notas de R$ 1'
"""


def calcular_troco(valor: int) -> str:
    """Escreva aqui em baixo a sua solução"""
    tipos_de_notas = [1, 5, 10, 50, 100]
    resto = valor
    troco = []
    while resto > 0:
        tipo_de_nota = tipos_de_notas.pop()
        pedacos = divmod(resto, tipo_de_nota)
        numero_notas, resto = pedacos
        if numero_notas>0:
            troco.append((numero_notas, tipo_de_nota))
    resultado = ''
    aux=0
    for v in troco:
        qntd, nota = v
        aux+=1
        if len(troco) == 1:
            if qntd > 1:
                resultado += f'{qntd} notas de R$ {nota}'
            else:
                resultado += f'{qntd} nota de R$ {nota}'
        elif aux == len(troco)-1:
            if qntd > 1:
                resultado += f'{qntd} notas de R$ {nota} '
            else:
                resultado += f'{qntd} nota de R$ {nota} '
        elif aux == len(troco) and len(troco) > 1:
            if qntd > 1:
                resultado += f'e {qntd} notas de R$ {nota}'
            else:
                resultado += f'e {qntd} nota de R$ {nota}'
        else:
            if qntd > 1:
                resultado += f'{qntd} notas de R$ {nota}, '
            else:
                resultado += f'{qntd} nota de R$ {nota}, '
    print(f"'{resultado}'")
