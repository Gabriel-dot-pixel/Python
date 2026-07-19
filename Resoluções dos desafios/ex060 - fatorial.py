'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex:
5! = 5x4x3x2x1 = 120
'''
print(f'{" DESAFIO 060 ":=^25}')
n = int(input('Digite o número que você quer saber o fatorial: '))
print(f'O fatorial de {n} é igual a', end=' ')
if n > 1:
    a = n - 1
else:
    a = 1
while a >= 1:
    n *= a
    a -= 1
print(n)
# Versão usando for
n = int(input('Digite o número que você quer saber o fatorial: '))
print(f'O fatorial de {n} é igual a', end=' ')
for i in range(n-1, 0, -1):
    n *= i
print(n)
