# Faça um programa que mostre na tela a contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles
from time import sleep
print('====== DESAFIO 046 ======')
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('FELIZ ANO NOVO!🥳🎉🎆🎆🎆')
