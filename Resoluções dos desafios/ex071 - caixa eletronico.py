# Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usúario qual o valor a ser sacado (valor inteiro) e o programa vai informar quantas cedulas de cada valor serão entregues. OBS: Considere que o caixa possui cedulas de R$50, R$20, R$10 e R$1
print(f'{" DESAFIO 071 ":=^25}')
valor = int(input('Qual o valor que você quer sacar? R$'))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Você vai receber {totalced} notas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
