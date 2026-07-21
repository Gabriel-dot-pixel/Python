# Faça um programa que jogue par ou impar com o computador. O jogo só sera interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
from random import randint
print(f'{" DESAFIO 068 ":=^25}')
vitoria = 0
while True:
    n = int(input('Digite um valor: '))
    pi = str(input('Par ou Ímpar? (P/I) ')).strip().upper()[0]
    while pi not in 'PI':
        pi = str(input('\033[31mVALOR INVÁLIDO!\033[m Digite novamente: ')).strip().upper()[0]
    computador = randint(0, 10)
    soma = n + computador
    if pi == 'P':
        if soma % 2 == 0:
            print('=' * 20)
            print(f'Você jogou {n} e o computador jogou {computador}. Total deu {soma}, que é PAR')
            print('=' * 20)
            print('Você VENCEU')
            vitoria += 1
        else:
            print('=' * 20)
            print(f'Você jogou {n} e o computador jogou {computador}. Total deu {soma}, que é ÍMPAR')
            print('=' * 20)
            break
    elif pi == 'I':
        if soma % 2 == 1:
            print('=' * 20)
            print(f'Você jogou {n} e o computador jogou {computador}. Total deu {soma}, que é ÍMPAR')
            print('=' * 20)
            print('Você VENCEU')
            vitoria += 1
        else:
            print('=' * 20)
            print(f'Você jogou {n} e o computador jogou {computador}. Total deu {soma}, que é PAR')
            print('=' * 20)
            break
    print('Vamos jogar denovo...')
print(f'GAME OVER! Você ganhou {vitoria} vezes')
