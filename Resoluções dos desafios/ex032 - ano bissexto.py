# Faça um programa que leia um ano qualquer e mostre se ele é bissexto
from datetime import date
print('====== DESAFIO 032 ======')
ano = int(input('Digite o ano que você quer analisar (digite 0 se você quiser analisar o ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0:
    if ano % 100 != 0:
        print(f'{ano} é bissexto')
    else:
        if ano % 400 == 0:
            print(f'{ano} é bissexto')
        else:
            print(f'{ano} não é bissexto')
else:
    print(f'{ano} não é bissexto')
