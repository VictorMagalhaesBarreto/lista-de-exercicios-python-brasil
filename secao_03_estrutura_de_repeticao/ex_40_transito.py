"""
Exercício 40 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
1) seguintes dados:
2) Código da cidade;
3) Número de veículos de passeio (em 1999);
4) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:

1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
2) Qual a média de veículos nas cinco cidades juntas;
3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

Mostre os valores com uma casa decimail

    >>> calcular_estatisticas(('SJC', 190_000, 300), ('SP', 1_000_000, 2_000 ),
    ... ('BH', 800_000, 1000), ('FZ', 600_000, 700), ('FL', 150_000, 900)
    ... )
    O maior índice de acidentes é de FL, com 6.0 acidentes por mil habitantes.
    O menor índice de acidentes é de FZ, com 1.2 acidentes por mil habitantes.
    O média de veículos por cidade é de 548000.
    A média de acidentes total nas cidades com menos de 150 mil habitantes é de 900.0 acidentes.
"""

from statistics import mean

def calcular_estatisticas(*cidades):
    """Escreva aqui em baixo a sua solução"""
    lista_codigo = []
    lista_numero_veiculos = []
    lista_numero_acidentes = []
    cidades_abaixo_150 = []
    acidentes_veiculos = []
    a = []
    for codigo, veiculos, acidentes in cidades:
        lista_codigo.append(codigo)
        lista_numero_veiculos.append(veiculos)
        a.append(acidentes / veiculos * 1000)
        if veiculos <= 150_000:
            cidades_abaixo_150.append(acidentes)
    codigo_acidentes = {acidentes:codigo for codigo, acidentes in zip(lista_codigo, a)}
    maior = max(codigo_acidentes)
    menor = min(codigo_acidentes)
    nome_maior = codigo_acidentes[maior]
    nome_menor = codigo_acidentes[menor]
    media_veiculos = mean(lista_numero_veiculos)
    media_acidentes = mean(cidades_abaixo_150)
    print(f'O maior índice de acidentes é de {nome_maior}, com {maior:.1f} acidentes por mil veículos.')
    print(f'O menor índice de acidentes é de {nome_menor}, com {menor:.1f} acidentes por mil veículos.')
    print(f'O média de veículos por cidade é de {media_veiculos}.')
    print(f'A média de acidentes total nas cidades com menos de 150 mil habitantes é de {media_acidentes:.1f}')






