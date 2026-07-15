'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço normal
– 3x ou mais no cartão: 20% de juros
'''
print('====== DESAFIO 044 ======')
preco = float(input('Qual o preço do produto? R$'))
forma = str(input('Qual vai ser a forma de pagamento? ')).strip().lower()
if forma == 'a vista em dinheiro' or forma == 'a vista em cheque':
    desconto = preco - (preco * 0.1)
    print(f'Você ganhou 10% de desconto, o preço final do produto é R${desconto:.2f}')
elif forma == 'a vista no cartão':
    desconto = preco - (preco * 0.05)
    print(f'Você ganhou 5% de desconto, o preço final do produto é R${desconto:.2f}')
elif forma == 'em até 2x no cartão':
    print(f'Você vai pagar o preço normal do produto, R${preco:.2f}')
elif forma == '3x ou mais no cartão':
    juros = preco * 1.20
    print(f'Você vai pagar 20% a mais de juros, o preco final do produto é R${juros:.2f}')
