"""
Exercício 37 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais 
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu nome, sua altura e 
seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo nome. Ao encerrar o programa 
também deve ser informados os nomes e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além
da média das alturas e dos pesos dos clientes
 
    >>> from secao_03_estrutura_de_repeticao import ex_37_senso_de_academia
    >>> entradas = ['0', '81', '162', 'Renzo']  # Um aluno apenas
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Renzo, com 162 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Renzo, com 81 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 162.0 centímetros
    Media de peso dos clientes: 81.0 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 177.0 centímetros
    Media de peso dos clientes: 80.5 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.7 centímetros
    Media de peso dos clientes: 103.7 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota', '50', '172', 'Seco']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Seco, com 50 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.0 centímetros
    Media de peso dos clientes: 90.2 kilos

"""
from statistics import mean

def rodar_senso():
    """Escreva aqui em baixo a sua solução"""
    lista_nomes = []
    lista_alturas = []
    lista_pesos = []
    nome = ''
    while nome != '0':
        nome = str(input(''))
        if nome == '0':
            break
        altura = str(input(''))
        peso = str(input(''))
        lista_nomes.append(nome)
        lista_alturas.append(float(altura))
        lista_pesos.append(float(peso))
    nome_altura = {altura:nome for nome, altura in zip(lista_nomes, lista_alturas)}
    maior_altura = max(nome_altura)
    menor_altura = min(nome_altura)
    nome_maior_altura = nome_altura[maior_altura]
    nome_menor_altura = nome_altura[menor_altura]
    nome_peso = {peso: nome for nome, peso in zip(lista_nomes, lista_pesos)}
    maior_peso = max(nome_peso)
    menor_peso = min(nome_peso)
    nome_maior_peso = nome_peso[maior_peso]
    nome_menor_peso = nome_peso[menor_peso]
    media_alturas = mean(lista_alturas)
    media_pesos = mean(lista_pesos)
    print(f'Cliente mais alto: {nome_maior_altura}, com {maior_altura:.0f} centímetros')
    print(f'Cliente mais baixo: {nome_menor_altura}, com {menor_altura:.0f} centímetros')
    print(f'Cliente mais magro: {nome_menor_peso}, com {menor_peso:.0f} kilos')
    print(f'Cliente mais gordo: {nome_maior_peso}, com {maior_peso:.0f} kilos')
    print(f'--------------------------------------------------')
    print(f'Media de altura dos clientes: {media_alturas:.1f} centímetros')
    print(f'Media de peso dos clientes: {media_pesos:.1f} kilos')

