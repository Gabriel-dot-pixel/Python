# Crie um programa que leia um número real qualquer e mostre na tela a sua porção inteira. 
# Ex: Digite um número: 6.127 -> O número 6.127 tem a parte inteira 6
from math import trunc
print('====== DESAFIO 016 ======')
num = float(input('Digite um número: '))
inteiro = trunc(num)
print(f'A parte inteira de {num} é {inteiro}')
# print(f'A parte inteira de {num} é {int(num)}') -> função padrão do python sem importação de biblioteca
