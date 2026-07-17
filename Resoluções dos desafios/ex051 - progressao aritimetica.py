# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão
print(f'{" DESAFIO 051 ":=^25}')
i = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
d = i + (10-1) * r
print('Os 10 primeiros termos da progressão são:')
for c in range(i, d + r, r):
    print(c)
