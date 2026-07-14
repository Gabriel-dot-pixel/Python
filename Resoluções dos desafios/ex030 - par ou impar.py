# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar
print('====== DESAFIO 030 ======')
n = int(input('Digite um número: '))
if n % 2 == 0:
    print(f'{n} é par')
else:
    print(f'{n} é ímpar')
