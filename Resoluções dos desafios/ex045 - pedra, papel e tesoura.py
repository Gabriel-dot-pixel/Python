# Crie um programa que faça o computador jogar Pedra, Papel e Tesoura com você
from random import randint
print('====== DESAFIO 045 ======')
mao = int(input('Digite qual mão você quer jogar (1 - Pedra; 2 - Papel; 3 - Tesoura): '))
aleatorio = randint(1, 3)
if mao == 1 and aleatorio == 3:
    print('Você ganhou! Você jogou Pedra e o computador jogou Tesoura')
elif mao == 1 and aleatorio == 2:
    print('Você perdeu! Você jogou pedra e o computador jogou Papel')
elif mao == 2 and aleatorio == 1:
    print('Você ganhou! Você jogou Papel e o computador jogou Pedra')
elif mao == 2 and aleatorio == 3:
    print('Você perdeu! Você jogou Papel e o computador jogou Tesoura')
elif mao == 3 and aleatorio == 2:
    print('Você ganhou! Você jogou Tesoura e o computador jogou Papel')
elif mao == 3 and aleatorio == 1:
    print('Você perdeu! Você jogou Tesoura e o computador jogou Pedra')
elif mao == aleatorio:
    print('Deu empate! Você e o computador jogaram a mesma mão')
