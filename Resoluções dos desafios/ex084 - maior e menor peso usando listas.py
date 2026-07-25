'''
Faça um programa que leia o nome e o peso de varias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) Uma listagem com as pessoas mais pessadas
C) Uma listagem com as pessoas mais leves
'''
pessoas = []
dados = []
while True:
    print('=' * 30)
    print(f'{"CADASTRO DE PESSOAS":^30}')
    print('=' * 30)
    dados.append(str(input('Nome: ').strip()))
    dados.append(float(input('Peso: (kg) ')))
    pessoas.append(dados[:])
    dados.clear()
    r = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('\033[31mVALOR INVÁLIDO!\033[m Digite novamente: ')).strip().upper()[0]
    if r == 'N':
        break
print(f'{" RESULTADOS ":=^30}')
print(f'As pessoas cadastradas foram: {pessoas}')
print(f'Foram cadastradas ao todo {len(pessoas)} pessoas')
maior = pessoas[0][1]
menor = pessoas[0][1]
for p in pessoas:
    if p[1] > maior:
        maior = p[1]
    elif p[1] < menor:
        menor = p[1]
print(f'O maior peso cadastrado foi {maior:.1f} Kg. Pertencente a', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print(f'\nO menor peso cadastrado foi {menor:.1f} Kg. Pertencente a', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
