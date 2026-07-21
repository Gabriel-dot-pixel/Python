# Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usúario qual o valor a ser sacado (valor inteiro) e o programa vai informar quantas cedulas de cada valor serão entregues. OBS: Considere que o caixa possui cedulas de R$50, R$20, R$10 e R$1
print(f'{" DESAFIO 071 ":=^25}')
n = int(input('Quanto você quer sacar? R$'))
quant50 = n / 50
n = n % 50
quant20 = n / 20
n = n % 20
quant10 = n / 10
n = n % 10
quant1 = n / 1
n = n % 1
if quant50 > 0.9:
    print(f'Você vai receber {quant50} notas de 50')
if quant20 > 0.9:
    print(f'Você vai receber {quant20} notas de 20')
if quant10 > 0.9:
    print(f'Você vai receber {quant10} notas de 10')
if quant1 > 0.9:
    print(f'Você vai receber {quant1} notas de 1')
