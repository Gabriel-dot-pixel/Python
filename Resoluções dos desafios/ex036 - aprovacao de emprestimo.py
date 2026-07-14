'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''
print('====== DESAFIO 036 ======')
casa = float(input('Qual o valor da casa que você quer comprar? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos você pretende pagar o empréstimo? '))
prestacao = casa / (anos * 12)
percent = salario - (salario * 0.3)
if prestacao <= percent:
    print('Parabéns! O seu empréstimo foi aprovado!', end=' ')
    print(f'Você vai pagar {anos*12} prestações de R${prestacao:.2f}')
else:
    print('Infelizmente, o seu empréstimo foi recusado', end=' ')
    print('pois o valor da prestação do empréstimo foi maior que 30% do seu salário')
    print(f'A prestação ficou em R${prestacao:.2f} e o percentual do seu salário era R${percent:.2f}')
