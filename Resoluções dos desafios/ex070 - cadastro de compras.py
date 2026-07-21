'''
Crie um programa que leia o nome e o preço de vários produtos. O programa devera perguntar se o usuario vai continuar. No final, mostre:
A) Qual é o total gasto na compra
B) Quantos produtos custam mais de R$1.000,00
C) Qual é o nome do produto mais barato
'''
print(f'{" DESAFIO 070 ":=^25}')
quant = 1
total = 0.0
mil = 0
precobarato = 0.0
nomeprodutobarato = ''
while True:
    print(f'---- {quant}ª Produto ----')
    nome = str(input('Nome: ')).strip()
    preco = float(input('Preço: R$'))
    if preco > 1000.0:
        mil += 1
    if quant == 1 or preco < precobarato:
        nomeprodutobarato = nome
        precobarato = preco
    quant += 1
    total += preco
    r = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
    if r == 'N':
        break
    while r not in 'SN':
        r = str(input('\033[31mVALOR INVÁLIDO!\033[m Digite novamente: ')).strip().upper()[0]
print(f'O total da compra foi R${total:.2f}')
print(f'{mil} produtos custam mais de R$1.000')
print(f'O produto mais barato custa R${precobarato:.2f} e é um(a) {nomeprodutobarato}')