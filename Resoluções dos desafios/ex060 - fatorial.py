'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex:
5! = 5x4x3x2x1 = 120
'''
# Da pra usar tambem o método factorial() do módulo math
print(f'{" DESAFIO 060 ":=^25}')
# Versão usando while
n = int(input('Digite o número que você quer saber o fatorial: '))
print(f'{n}! =', end=' ')
a = n
f = 1
while a > 0:
    print(f'{a}', end='')
    if a > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f *= a
    a -= 1
print(f)
# Versão usando for
n = int(input('Digite o número que você quer saber o fatorial: '))
print(f'{n}! =', end=' ')
f = 1
for i in range(n, 0, -1):
    print(f'{i}', end='')
    if i > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f *= i
print(f)
