'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço normal
– 3x ou mais no cartão: 20% de juros
'''
print('====== DESAFIO 044 ======')
preco = float(input('Qual o valor da compra? R$'))
print('Aqui estão as formas de pagamento:')
print('1 - á vista em dinheiro/cheque')
print('2 - á vista no cartão')
print('3 - 2x no cartão')
print('4 - 3x ou mais no cartão')
opc = int(input('Digite a opção que gostaria de pagar: '))
if opc == 1:
    desconto = preco - (preco * 0.1)
    print(f'A sua compra que estava custando R${preco:.2f} vai passar a custar R${desconto:.2f}')
elif opc == 2:
    desconto = preco - (preco * 0.05)
    print(f'A sua compra que estava custando R${preco:.2f} vai passar a custar R${desconto:.2f}')
elif opc == 3:
    print(f'Você vai pagar R${preco:.2f}')
elif opc == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = preco * 1.20
    parc = (preco / parcelas) * 1.20
    print(f'Você vai pagar {parcelas} parcelas de R${parc:.2f}, contando juros, que vão totalizar R${juros:.2f}')
else:
    print('Opção inválida!')
