'''
Esceva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usúario tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usúario venceu ou perdeu.
'''
from random import randint
from time import sleep
print('====== DESAFIO 028 ======')
aleatorio = randint(0, 5)
print('-=-' * 20)
print('Estou pensando em um número entre 0 e 5...')
print('-=-' * 20)
sleep(2)
chute = int(input('Em que número eu pensei? '))
if chute == aleatorio:
    print(f'Você venceu! O número que eu estava pensando era {aleatorio}')
else:
    print(f'Eu venci! O número que eu estava pensando era {aleatorio} e não {chute}')
