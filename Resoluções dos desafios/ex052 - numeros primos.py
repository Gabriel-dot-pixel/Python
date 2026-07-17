# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
print(f'{" DESAFIO 052 ":=^25}')
n = int(input('Digite um número: '))
t = 0
for i in range(1, n+1):
    if n % i == 0:
        t += 1
if t == 2:
    print(f'{n} é primo')
else:
    print(f'{n} não é primo')
