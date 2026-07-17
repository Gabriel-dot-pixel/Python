# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas ja são maiores
from datetime import date
print(f'{" DESAFIO 054 ":=^25}')
hoje = date.today().year
maior = 0
menor = 0
for i in range(1, 8):
    nasc = int(input(f'Digite o ano de nascimento da pessoa {i}: '))
    if hoje - nasc < 21:
        menor += 1
    else:
        maior += 1
print(f'Dessas 7 pessoas: {menor} não atingiram a maioridade e {maior} ja são maiores')