# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o
print(f'{" DESAFIO 050 ":=^25}')
s = 0
for i in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s += n
print(f'Soma de todos os números pares que você digitou: {s}')
