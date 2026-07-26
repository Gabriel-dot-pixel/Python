# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionários. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado
from random import randint
jogadores = dict()
jogo = list()
for i in range(0,4):
    dado = randint(1, 6)
    jogadores['jogador'] = f'jogador{i+1}'
    jogadores['resultado'] = dado
    jogo.append(jogadores.copy())
print('Valores sorteados:')
for i in range(0, 4):
    print(f'O jogador {jogo[i]['jogador']} tirou {jogo[i]['resultado']}')
