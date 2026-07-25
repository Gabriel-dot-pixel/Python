# Crie um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado. No final mostre a matriz na tela, com a formatação correta
matriz = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f'Digite um valor para a posição [{i}][{j}]: '))
        matriz[i].append(n)
print('=' * 40)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[i][j]} ]', end='')
    print()
