# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer
from random import randint
from time import sleep
print(f'{" DESAFIO 058 ":=^25}')
computador = randint(0, 10)
print('-=-' * 20)
print('Estou pensando em um número entre 0 e 10...')
print('-=-' * 20)
sleep(2)
palpite = int(input('Em que número eu pensei? '))
tentativa = 0
while palpite != computador:
    palpite = int(input('Você errou, tente novamente: '))
    tentativa += 1
print(f'Parabéns! Você acertou, mas precisou de {tentativa} tentativas para ganhar')
