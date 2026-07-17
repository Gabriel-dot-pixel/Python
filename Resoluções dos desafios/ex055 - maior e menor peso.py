# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido
print(f'{" DESAFIO 055 ":=^25}')
peso = float(input('Digite o peso da pessoa 1: (kg)'))
maior = peso
menor = peso
for i in range(2,6):
    peso = float(input(f'Digite o peso da pessoa {i}: (kg) '))
    if peso > maior:
        maior = peso
    else:
        menor = peso
# print(f'O maior peso lido foi {maior:.1f}kg')
print(f'O menor peso lido foi {menor:.1f}kg')
