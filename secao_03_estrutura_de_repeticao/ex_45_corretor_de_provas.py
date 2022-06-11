"""
Exercício 45 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno
a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a
nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma com uma casa decimal.

Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

    >>> corrigir(('Renzo','A','B','C','D','E','E','D','C','B','A' ))
    Aluno                 Nota
    Renzo                 10
    ---------------------------
    Média geral: 10.0
    Maior nota: 10
    Menor nota: 10
    Total de Alunos: 1
    >>> corrigir(
    ... ('Renzo','A','B','C','D','E','E','D','C','B','A' ),
    ... ('Fulano','A','B','C','D','E','E','D','C','B','B' ),
    ... )
    Aluno                 Nota
    Renzo                 10
    Fulano                 9
    ---------------------------
    Média geral: 9.5
    Maior nota: 10
    Menor nota: 9
    Total de Alunos: 2
"""

from statistics import mean

def corrigir(*provas):
    """Escreva aqui em baixo a sua solução"""
    resultados = {}
    gabarito = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"E", 7:"D", 8:"C", 9:"B", 10:"A"}
    for prova in provas:
        nota = 0
        aluno = prova[0]
        aux = 1
        for questao in prova[1:11]:
            if questao == gabarito[aux]:
                nota += 1
            aux += 1
        resultados[nota] = aluno
    media = mean(resultados)
    maior = max(resultados)
    menor = min(resultados)
    print('Aluno'.ljust(21),'Nota')
    for nota, nome in resultados.items():
        print(f'{nome}'.ljust(21),f'{nota}'.rjust(2))
    print('---------------------------')
    print(f'Média geral: {media:.1f}')
    print(f'Maior nota: {maior}')
    print(f'Menor nota: {menor}')
    print(f'Total de Alunos: {len(resultados)}')




