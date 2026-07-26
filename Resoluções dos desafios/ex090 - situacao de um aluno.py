# Faça um programa que leia o nome e a media de um aluno, guardando tambem a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela
aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip()
aluno['média'] = float(input(f'Média de {aluno['nome']}: '))
if aluno['média'] >= 6.0:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
print(f'Nome do aluno: {aluno["nome"]}')
print(f'Média do aluno: {aluno["média"]}')
print(f'Situação do aluno: {aluno["situação"]}')
