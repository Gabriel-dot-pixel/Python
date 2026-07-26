'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados
B) A soma dos valores da terceira coluna
C) O maior valor da segunda linha
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = 0
stercol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Posição [{l}][{c}]: '))
        if matriz[l][c] % 2 == 0:
            spar += n
print('=' * 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]} ]', end='')
    print()
print('=' * 40)
print(f'A soma de todos os valores pares digitados é: {spar}')
for l in range(0, 3):
    stercol += matriz[l][2]
print(f'A soma de todos os valores da terceira coluna é: {stercol}')
maior = matriz[1][0]
for c in range(0, 3):
    if matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é: {maior}')
