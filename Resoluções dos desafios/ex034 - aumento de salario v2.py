'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$1.250,00, calcule um aumento de 10%

Para os inferiores ou iguais, o aumento é de 15%
'''
print('====== DESAFIO 034 ======')
salario = float(input('Digite o seu salário: R$'))
if salario > 1250.0:
    aumento = salario * 1.10
else:
    aumento = salario * 1.15
print(f'O seu novo salário é R${aumento:.2f}')
