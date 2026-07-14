# Faça um programa que leia o comprimento do cateto oposto e o cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
from math import hypot
print('====== DESAFIO 017 ======')
a = int(input('Quanto mede o cateto oposto do triângulo? '))
b = int(input('Quanto mede o cateto adjacente do triângulo? '))
c = hypot(a, b)
print(f'O comprimento da hipotenusa mede {c:.2f}')

'''c = (a**2 + b**2)**(1/2)
print(f'O comprimento da hipotenusa mede {c:.0f}')'''
