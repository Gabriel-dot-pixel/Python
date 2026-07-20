# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer
from random import randint
from time import sleep
print(f'{" DESAFIO 058 ":=^25}')
computador = randint(0, 10)
print('-=-' * 20)
print('Estou pensando em um número entre 0 e 10...')
print('-=-' * 20)
sleep(2)
tentativa = 0
lFlag = False
while not lFlag:
    palpite = int(input('Em que número eu pensei? '))
    tentativa += 1
    if palpite == computador:
        lFlag = True
    else:
        if palpite < computador:
            palpite = int(input('Um pouco mais... Tenta denovo: '))
            tentativa += 1
        else:
            palpite = int(input('Um pouco menos... Tenta denovo: '))
            tentativa += 1
if tentativa == 1:
    print('Parabéns! Você acertou na primeira tentativa')
elif tentativa < 4:
    print(f'Parabéns! Você acertou e só precisou de {tentativa} tentativas para ganhar')
else:
    print(f'Parabéns! Você acertou, mas precisou de {tentativa} tentativas para ganhar')
