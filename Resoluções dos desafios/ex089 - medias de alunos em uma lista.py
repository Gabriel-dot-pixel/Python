# Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usúario possa mostrar as notas de cada aluno individualmente
ficha = []
while True:
    nome = str(input('Nome: ')).strip().title()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    r = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('\033[31mVALOR INVÁLIDO!\033[m Digite novamente: ')).strip().upper()[0]
    if r == 'N':
        break
print('=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    n = int(input('Mostrar as notas de qual aluno? (999 para interromper)'))
    if n == 999:
        print('Finalizando...')
        break
    if n <= len(ficha)-1:
        print(f'Notas de {ficha[n][0]} são {ficha[n][1]}')
    else:
        print('Aluno não encontrado...')
