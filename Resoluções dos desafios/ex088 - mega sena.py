# Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai gerar 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta
from random import randint
from time import sleep
print('=' * 40)
print(f'{"MEGA SENA":^40}')
print('=' * 40)
jogos = []
palpite = []
quant = int(input('Quantos jogos você quer fazer? '))
for i in range(0, quant):
    sleep(1)
    while len(palpite) < 6:
        aleatorio = randint(1, 60)
        if aleatorio not in palpite:
            palpite.append(aleatorio)
    jogos.append(palpite[:])
    palpite.clear()
    print(f'Jogo {i+1}: {jogos[i]}')
print(f'{" BOA SORTE! ":=^40}')
