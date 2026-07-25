# Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usúario possa mostrar as notas de cada aluno individualmente
alunos = []
dados = []
notas = []
while True:
    dados.append(str(input('Nome: ')).strip().title())
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    dados.append(notas[:])
    notas.clear()
    alunos.append(dados[:])
    dados.clear()
    r = str(input('Quer continuar? ')).strip().upper()[0]
    if r == 'N':
        break
