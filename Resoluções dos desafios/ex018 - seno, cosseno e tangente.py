# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import sin, cos, tan, radians
print('====== DESAFIO 018 ======')
a = float(input('Digite um ângulo: '))
angulo = radians(a)
seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)
print(f'O seno desse ângulo vale {seno:.2f}, o cosseno vale {cosseno:.2f} e a tangente vale {tangente:.2f}')
