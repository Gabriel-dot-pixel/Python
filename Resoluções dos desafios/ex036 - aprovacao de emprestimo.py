'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''
print('====== DESAFIO 036 ======')
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
percent = salario - (salario * 0.3)
if prestacao <= percent:
    print('Parabéns! O seu empréstimo foi aprovado!', end=' ')
    print(f'Você vai pagar {anos*12} prestações de R${prestacao:.2f}')
else:
    print(f'Infelizmente, o seu empréstimo foi recusado, pois a prestação ficou em R${prestacao:.2f}')
