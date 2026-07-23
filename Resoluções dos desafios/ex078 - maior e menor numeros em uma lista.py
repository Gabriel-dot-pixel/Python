'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista
'''
print(f'{" DESAFIO 078 ":=^25}')
numeros = []
for i in range(0, 5):
    n = float(input(f'Digite o {i+1}º número: '))
    numeros.append(n)
maior = max(numeros)
menor = min(numeros)
for pos, n in enumerate(numeros):
    if n == maior:
        print(f'O maior valor digitado foi {maior} e esta nas posições ', end='')
        print(f'{pos}... ')
    if n == menor:
        print(f'O menor valor digitado foi {menor} e esta nas posições ', end='')
        print(f'{pos}... ')
