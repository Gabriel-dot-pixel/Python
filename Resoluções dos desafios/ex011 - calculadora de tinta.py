# Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área e a quantidade de tinta para pinta-lá, sabendo que cada litro de tinta pinta uma área de 2m²
print('====== DESAFIO 011 ======')
a = float(input('Qual a altura da parede? '))
l = float(input('Qual a largura da parede? '))
ar =  a * l
t = ar / 2
print('A parede tem {:.2f}m², então serão necessários {:.2f}l de tinta para pinta-lá'.format(ar, t))
