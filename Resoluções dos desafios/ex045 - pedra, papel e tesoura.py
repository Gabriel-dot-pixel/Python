# Crie um programa que faça o computador jogar Pedra, Papel e Tesoura com você
from random import randint
from time import sleep
print('====== DESAFIO 045 ======')
itens = ('Pedra', 'Papel', 'Tesoura')
print('Suas opções:')
print('0 - Pedra')
print('1 - Papel')
print('2 - Tesoura')
mao = int(input('Digite qual opção você quer jogar: '))
print('PEDRA')
sleep(0.5)
print('PAPEL')
sleep(0.5)
print('TESOURA!!!')
sleep(0.5)
computador = randint(1, 3)
print('-=' * 10)
print(f'O computador jogou {itens[computador]}')
print(f'Você jogou {itens[mao]}')
print('-=' * 10)
if computador == 0:
    if mao == 0:
        print('EMPATE')
    elif mao == 1:
        print('Você VENCEU')
    elif mao == 2:
        print('Computador VENCEU')
    else:
        print('Jogada inválida')
elif computador == 1:
    if mao == 0:
        print('Computador VENCEU')
    elif mao == 1:
        print('EMPATE')
    elif mao == 2:
        print('Você VENCEU')
    else:
        print('Jogada inválida')
elif computador == 2:
    if mao == 0:
        print('Você VENCEU')
    elif mao == 1:
        print('Computador VENCEU')
    elif mao == 2:
        print('EMPATE')
    else:
        print('Jogada inválida')
